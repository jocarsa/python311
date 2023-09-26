#pip install flask
from flask import Flask, render_template

edad = 45

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return render_template("index.html")

@aplicacion.route('/damedatos')
def damedatos():
    global edad
    edad += 1
    return "Yo soy Python y tu edad es de: "+str(edad)+" años"


if __name__ == '__main__':
    aplicacion.run(host="192.168.1.215")
