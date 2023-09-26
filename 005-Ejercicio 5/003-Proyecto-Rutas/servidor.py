#pip install flask
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return "Estás viendo la página de inicio"

@aplicacion.route('/sobremi')
def sobremi():
    return "Estás viendo la página de sobre mi"

@aplicacion.route('/contacto')
def contacto():
    return "Estás viendo la página de contacto"

if __name__ == '__main__':
    aplicacion.run()
