import os

carpeta = input("Introduce la carpeta donde buscar:")
palabra = input("Introduce el término que buscar:")

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
