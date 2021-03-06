from wtforms import Form
from wtforms import HiddenField
from wtforms import StringField
from wtforms import validators
from wtforms.fields.html5 import EmailField


# Validacion personalizada
def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class CommentForm(Form):
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
    comment = StringField('Comment')
    honeypot = HiddenField('', [length_honeypot])