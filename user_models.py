import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from wtforms import Form
from wtforms import HiddenField
from wtforms import StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(100))
    comments = db.relationship('Comment')  # no se crea columna en bd, es para relacionar con python
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.create_password(password)

    def create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class UserForm(Form):
    username = StringField('Username',
                           [
                               validators.required(message='Username es requerido'),
                               validators.length(min=4, max=25, message='Ingresa un username correcto')
                           ])
    email = EmailField('E-mail',
                       [
                           validators.required(message='Email es requerido'),
                           validators.email(message='Ingresa un mail valido')
                       ])
    password = StringField('Password')
    honeypot = HiddenField('', [length_honeypot])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise validators.ValidationError('El username ya se encuentra registrado!')
