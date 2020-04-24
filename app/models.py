from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    messages = db.relationship('Message', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'))

    def __repr__(self):
        return f'<Message {self.body}>'

class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chatroom_name = db.Column(db.String(64), unique=True)
    messages = db.relationship('Message', backref='chatroom', lazy='dynamic')

    def __repr__(self):
        return f'<Chatroom {self.chatroom_name}>'
