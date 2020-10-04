import datetime

from flask_sqlalchemy import SQLAlchemy
from wtforms import Form
from wtforms import HiddenField
from wtforms import StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.create_password(password)

    def create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

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
