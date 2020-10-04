#!/usr/bin/env python
import json

from flask import Flask
from flask import flash
from flask import g
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_wtf import CSRFProtect

import user_login
from config import DevelopmentConfig
from user_models import User
from user_models import UserForm
from user_models import db

app = Flask(__name__, template_folder='files_html')
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)


@app.errorhandler(401)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    print('Before request')
    print(request.base_url)
    print(request.access_route)
    print(request.endpoint)
    # if 'username' not in session:


@app.after_request
def after_request(response):
    print('after request')
    return response


@app.route('/')
def index():
    # if no found custome_cookie return value_undefined
    custome_cookie = request.cookies.get('custome_cookie', 'value_undefined')
    print('custome_cookie = ', custome_cookie)
    if 'username' in session:
        username = session['username']
        print('username ', username)
    return render_template('index.html')


@app.route('/users', methods=['POST', 'GET'])
def users():
    user_form = UserForm(request.form)
    if request.method == 'POST' and user_form.validate():
        user = User(username=user_form.username.data,
                    email=user_form.username.data,
                    password=user_form.password.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado'
        flash(success_message)
    return render_template('create_user.html', title='Create user', form=user_form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = user_login.LoginForm(request.form)
    print(login_form.username.data)
    print(login_form.password.data)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] = login_form.username.data
            return redirect(url_for('users'))
        else:
            error_message = 'Usuario o password no validos!'
            flash(error_message)

    return render_template('login.html', title='login', form=login_form)


@app.route('/cookie/')
def cookie():
    # las cookies trabajan sobre el objeto response
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Marcos Santiago Leonardo')
    return response


@app.route('/logout/')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('f_login'))


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    # mi validacion
    response = {'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(port=8000)
