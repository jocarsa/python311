import os

for root, dirnames, filenames in os.walk('carpeta'):
    print("He encontrado un archivo")
    print("La carpeta se llama:")
    print(root)
    print("Dentro de la carpeta están los siguientes directorios:")
    print(dirnames)
    print("Dentro del directorio estan los siguientes archivos:")
    print(filenames)


##archivo = open("carpeta/archivo.txt","r")
##
##contenido = archivo.read()
##print(contenido)
##
##encontrado = contenido.find("texto")
##if encontrado >= 0:
##    print("Se ha encontrado coincidencia")
##    reemplazo = contenido.replace("texto","gato")
##    archivo.close()
##    archivo = open("carpeta/archivo.txt","w")
##    archivo.write(reemplazo)
##    archivo.close()
##    
##else:
##    print("No se ha encontrado coincidencia")
##    archivo.close()
