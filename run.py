from flask import Flask
from flask import render_template
from flask import request
import form

# Nuevo objeto
# wrap o decorador de ruta
app = Flask(__name__, template_folder='files_html')


@app.route('/')
def index():
    return 'Hello world'


@app.route('/comments', methods=['GET'])
def comment():
    comment_form = form.CommentForm()
    return render_template('form.html', title='Comments', form=comment_form)


@app.route('/comments/', methods=['POST'])
def save_comment():
    comment_form = form.CommentForm(request.form)

    if comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en el formulario')

    return render_template('form.html', title='Comments', form=comment_form)


# Levanta  el servidor app.run() default port, and mode debug false
if __name__ == '__main__':
    app.run(debug=True)
