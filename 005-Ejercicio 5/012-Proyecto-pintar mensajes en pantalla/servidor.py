#pip install flask
from flask import Flask, render_template,request

mensajes = []

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return render_template("index.html")

@aplicacion.route('/envia')
def envia():
    global mensajes
    print("alguien me esta intentando enviar algo")
    mensajes.append(request.args.get('mensaje'))
    print(mensajes)
    return "ok"

@aplicacion.route('/recibe')
def recibe():
    return mensajes

if __name__ == '__main__':
    aplicacion.run(host="192.168.1.215")
