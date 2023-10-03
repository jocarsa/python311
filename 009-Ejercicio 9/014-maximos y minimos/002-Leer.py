from PIL import Image
import matplotlib.pyplot as plt

def histograma(ruta):
    imagen = Image.open(ruta)
    pixels = imagen.load()

    anchura = imagen.width
    altura= imagen.height
    rango = []
    etiquetas = []
    for r in range(0,255):
        rango.append(0)
        etiquetas.append(r)
    
    for x in range(0,anchura):
        for y in range(0,altura):
            color = imagen.getpixel((x,y))
            gris = round((color[0]+color[1]+color[2])/3)-1
            rango[gris] += 1
    
    print(rango)

##    plt.bar(etiquetas, rango, color='skyblue')
##    plt.title("histograma")
##    plt.show()

    maximo = 0
    for numero in rango:
        if numero > maximo:
            maximo = numero
    print(maximo)
    umbral = 0.05
    minimo = maximo*umbral

    #encontramos el tope por la izquierda
    for i in range(0,len(rango),1):
        if rango[i] > minimo:
            print("el tope esta en "+str(i))
            break
    #encontramos el tope por la derecha
    for i in range(len(rango)-1,0,-1):
        if rango[i] > minimo:
            print("el tope esta en "+str(i))
            break
    
    imagen.close()
    
histograma("foto.jpg")


