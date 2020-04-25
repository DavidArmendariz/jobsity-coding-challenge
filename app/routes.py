from flask import render_template, flash, redirect, url_for, request
from app import app, db, socketio, stock_rpc_client
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user
from app.models import User, Message, Chatroom
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse
from flask_socketio import SocketIO
from chatbot.validations import command_is_valid, stock_response
import threading


@app.route('/')
@app.route('/lobby')
@login_required
def lobby():
    chatrooms = list(
        map(lambda chatroom: chatroom.chatroom_name, Chatroom.query.all()))
    return render_template('lobby.html', title='Lobby', chatrooms=chatrooms)


@app.route('/chatroom/<chatroom_name>')
@login_required
def chatroom(chatroom_name):
    chatroom = Chatroom.query.filter_by(chatroom_name=chatroom_name).first()
    messages = Message.query.filter_by(chatroom_id=chatroom.id)\
        .order_by(Message.timestamp).limit(50).all()
    return render_template('chatroom.html', title=chatroom.chatroom_name, messages=messages,
                           chatroom=chatroom.chatroom_name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('lobby'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid credentials')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('lobby')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You signed up successfully! Login with your new credentials.')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)


@socketio.on('receive message')
def handle_message(message, methods=['GET', 'POST']):
    text = message['message']
    response = {'username': current_user.username, 'body': text}
    socketio.emit('message response', response)
    chatroom = Chatroom.query.filter_by(
        chatroom_name=message['chatroom']).first()
    message = Message(body=text, user=current_user, chatroom=chatroom)
    db.session.add(message)
    db.session.commit()


@socketio.on('receive command')
def handle_command(message, methods=['GET', 'POST']):
    command = message['message']
    if command_is_valid(command):
        try:
            stock_code = command.split('=')[1].upper()
            body = stock_rpc_client.call(stock_code)
            body = stock_response(stock_code, body)
        except:
            body = stock_response(stock_code, 'error')
    else:
        body = 'Invalid command. Check that it matches the syntax "/stock=stock_code"'
    response = {'username': 'Bot', 'body': body}
    socketio.emit('command response', response)
