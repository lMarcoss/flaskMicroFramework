from flask import Flask

# Nuevo objeto
# wrap o decorador de ruta
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


# Levanta  el servidor app.run() default port, and mode debug false
if __name__ == '__main__':
    app.run(debug=True)
