#pip install flask
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return 'Hola mundo desde Flask!'

if __name__ == '__main__':
    aplicacion.run()
