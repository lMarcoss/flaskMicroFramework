from wtforms import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import validators


class LoginForm(Form):
    username = StringField('Username',
                           [
                               validators.required(message='El username es requerido'),
                               validators.length(min=4, max=25, message='Ingresa un username correcto')
                           ])
    password = PasswordField('Password',
                             [
                                 validators.required('El password es requerido')
                             ])
