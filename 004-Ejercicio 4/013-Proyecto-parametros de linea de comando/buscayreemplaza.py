import os
import sys

carpeta = sys.argv[1]
palabra = sys.argv[2]

def busca(ruta,palabra):
    archivo = open(ruta,"r")
    contenido = archivo.read()
    resultado = contenido.find(palabra)
    if resultado >= 0:
        return True
    else:
        return False
    archivo.close()

for root, dirnames, filenames in os.walk(carpeta):
    for archivo in filenames:
        rutacompleta = os.path.join(root, archivo)
        try:
            if busca(rutacompleta,palabra) == True:
                print(rutacompleta," - ","encontrado")
        except:
            pass
