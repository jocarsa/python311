#pip install flask
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def hello_world():
    return '''
        <!doctype html>
        <html>
            <head>
            </head>
            <body>
                <h1>Hola mundo desde Python</h1>
            </body>
        </html>

    '''

if __name__ == '__main__':
    aplicacion.run()
