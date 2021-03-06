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

from user_models import db
from user_models import User

app = Flask(__name__, template_folder='files_html')
app.config.from_object(DevelopmentConfig)
# app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)


@app.errorhandler(401)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.test = 'test1'
    print('Before request')
    print(request.base_url)
    print(request.access_route)


@app.after_request
def after_request(response):
    print(g.test)
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


@app.route('/users', methods=['POST'])
def create_user():
    login_form = user_login.LoginForm(request.form)
    if login_form.validate():
        user = User(username=login_form.username.data,
                    password=login_form.password.data,
                    email=login_form.username.data)
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado'
        flash(success_message)
    return render_template('login.html', title='login', form=login_form)


@app.route('/login/', methods=['GET'])
def f_login():
    print(g.test)
    login_form = user_login.LoginForm()
    return render_template('login.html', title='login', form=login_form)


@app.route('/authentication/', methods=['POST'])
def authentication():
    login_form = user_login.LoginForm(request.form)
    if login_form.validate():
        username = login_form.username.data
        password = login_form.password.data


        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)

        print(login_form.username.data)
        print(login_form.password.data)

        session['username'] = login_form.username.data
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
