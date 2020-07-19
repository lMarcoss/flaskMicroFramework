from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello-world')
def hello_world():
    return 'Hello world'


@app.route('/welcome')
def welcome():
    return 'Welcome'


# http:localhost:5000/request?param1=value1&param2=value2
# http:localhost:5000/request
@app.route('/request')
def params():
    param = request.args.get('param1', 'value 1 is null')
    param2 = request.args.get('param2', 'value 2 is null')
    return 'El parametro1 es {} y el parametro2 es {}'.format(param, param2)


@app.route('/people/')
@app.route('/people/<name>/')
@app.route('/people/<name>/<int:age>/')
def books(name='no_value', age=0):
    return 'people: {} {}'.format(name, age)


if __name__ == '__main__':
    app.run(debug=True)
