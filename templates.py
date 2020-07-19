from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates_html')


@app.route('/hello-world')
def hello_world():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return 'Welcome'


@app.route('/people/')
@app.route('/people/<name>/')
@app.route('/people/<name>/<int:age>/')
def books(name='no_value', age=0):
    return 'people: {} {}'.format(name, age)


@app.route('/users/<user>/<int:age>')
def users(user, age):
    list = [1, 2, 3, 4, 6, 7, 5, 8]
    return render_template('user.html', nombre=user, age=age, list=list)


if __name__ == '__main__':
    app.run(debug=True)
