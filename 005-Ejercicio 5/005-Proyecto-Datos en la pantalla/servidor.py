#pip install flask
from flask import Flask, render_template

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return render_template("index.html")

@aplicacion.route('/damedatos')
def damedatos():
    return "Yo soy Python y te voy a dar datos"


if __name__ == '__main__':
    aplicacion.run()
