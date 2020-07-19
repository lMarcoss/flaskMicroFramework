from flask import Flask

# Nuevo objeto
# wrap o decorador de ruta
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


app.run()
