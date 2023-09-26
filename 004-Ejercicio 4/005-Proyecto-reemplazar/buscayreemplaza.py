archivo = open("carpeta/archivo.txt","r")

contenido = archivo.read()
print(contenido)

encontrado = contenido.find("texto")
if encontrado >= 0:
    print("Se ha encontrado coincidencia")
    reemplazo = contenido.replace("texto","gato")
    archivo.close()
    archivo = open("carpeta/archivo.txt","w")
    archivo.write(reemplazo)
    archivo.close()
    
else:
    print("No se ha encontrado coincidencia")
    archivo.close()
