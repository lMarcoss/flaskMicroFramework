from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_wtf import CSRFProtect

import login

app = Flask(__name__, template_folder='files_html')
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    # if no found custome_cookie return value_undefined
    custome_cookie = request.cookies.get('custome_cookie', 'value_undefined')
    print(custome_cookie)
    return render_template('index.html')


@app.route('/login/', methods=['GET'])
def show_form_login():
    login_form = login.LoginForm()
    return render_template('login.html', title='login', form=login_form)


@app.route('/authentication/', methods=['POST'])
def authentication():
    login_form = login.LoginForm(request.form)
    print(login_form.username.data)
    print(login_form.password.data)
    return render_template('login.html', title='login', form=login_form)


@app.route('/cookie/')
def cookie():
    # las cookies trabajan sobre el objeto response
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Marcos Santiago Leonardo')
    return response


# Levanta  el servidor app.run() default port, and mode debug false
if __name__ == '__main__':
    app.run(debug=True)
