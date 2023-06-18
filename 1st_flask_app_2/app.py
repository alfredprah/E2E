from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField('',[validators.DataRequired()])


@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form = form)

# this POST method will be used to transport the form data to the server in the message body
@app.route('/hello', methods = ['POST'])

# this function will render an HTML page hello.html if the form has been validated. 
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)