from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    messages = [
        {
            'user': {'username': 'David'},
            'body': 'Hola Diana!'
        },
        {
            'user': {'username': 'Diana'},
            'body': 'Hola David!'
        }
    ]
    return render_template('index.html', title='Chat Room', user=user, messages=messages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login successful')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
