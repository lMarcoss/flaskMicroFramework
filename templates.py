from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='files_html')


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
    return render_template('user.html', nombre=user, age=age)


@app.route('/clients')
def clients():
    clients_names = ['client1', 'client2', 'client3', 'client4', 'client5']
    return render_template('clients.html', clients=clients_names)


if __name__ == '__main__':
    app.run(debug=True)
