import os

def busca(ruta,palabra):
    archivo = open(ruta,"r")
    contenido = archivo.read()
    resultado = contenido.find(palabra)
    if resultado >= 0:
        return "encontrado"
    else:
        return "no encontrado"
    archivo.close()

for root, dirnames, filenames in os.walk('carpeta'):
    print("He encontrado un archivo")
    print("La carpeta se llama:")
    print(root)
    print("Dentro de la carpeta están los siguientes directorios:")
    print(dirnames)
    print("Dentro del directorio estan los siguientes archivos:")
    print(filenames)
    for archivo in filenames:
        rutacompleta = os.path.join(root, archivo)
        print(busca(rutacompleta,"otro"))
