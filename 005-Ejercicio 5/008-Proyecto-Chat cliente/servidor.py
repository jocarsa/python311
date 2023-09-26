#pip install flask
from flask import Flask, render_template,request

edad = 45

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return render_template("index.html")

@aplicacion.route('/envia')
def envia():
    print("alguien me esta intentando enviar algo: "+request.args.get('mensaje'))
    return "ok"


if __name__ == '__main__':
    aplicacion.run(host="192.168.1.215")
