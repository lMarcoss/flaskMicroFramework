from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CSRFProtect

import login

app = Flask(__name__, template_folder='files_html')
app.secret_key = 'my_secret_key'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello world'


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


# Levanta  el servidor app.run() default port, and mode debug false
if __name__ == '__main__':
    app.run(debug=True)
