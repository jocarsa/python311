archivo = open("carpeta/archivo.txt","r")

contenido = archivo.read()
print(contenido)

encontrado = contenido.find("platano")
print(encontrado)

archivo.close()
