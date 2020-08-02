from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from flask_wtf import CSRFProtect

import user_login

app = Flask(__name__, template_folder='files_html')
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)


@app.errorhandler(401)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    # if no found custome_cookie return value_undefined
    custome_cookie = request.cookies.get('custome_cookie', 'value_undefined')
    print('custome_cookie = ', custome_cookie)
    if 'username' in session:
        username = session['username']
        print('username ', username)
    return render_template('index.html')


@app.route('/login/', methods=['GET'])
def f_login():
    login_form = user_login.LoginForm()
    return render_template('login.html', title='login', form=login_form)


@app.route('/authentication/', methods=['POST'])
def authentication():
    login_form = user_login.LoginForm(request.form)
    if login_form.validate():
        session['username'] = login_form.username.data
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)

        print(login_form.username.data)
        print(login_form.password.data)

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


# Levanta  el servidor app.run() default port, and mode debug false
if __name__ == '__main__':
    app.run(debug=True)
