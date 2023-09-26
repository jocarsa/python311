import os

carpeta = input("Introduce la carpeta donde buscar:")
palabra = input("Introduce el término que buscar:")

def busca(ruta,palabra):
    archivo = open(ruta,"r")
    contenido = archivo.read()
    resultado = contenido.find(palabra)
    if resultado >= 0:
        return "encontrado"
    else:
        return "no encontrado"
    archivo.close()

for root, dirnames, filenames in os.walk(carpeta):
    for archivo in filenames:
        rutacompleta = os.path.join(root, archivo)
        print(rutacompleta," - ",busca(rutacompleta,palabra))
