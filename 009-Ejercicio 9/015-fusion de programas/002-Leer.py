from PIL import Image

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
    maximo = 0
    for numero in rango:
        if numero > maximo:
            maximo = numero
    umbral = 0.05
    minimo = maximo*umbral
    
    for i in range(0,len(rango),1):
        if rango[i] > minimo:
            tope1 = str(i)
            break
    for i in range(len(rango)-1,0,-1):
        if rango[i] > minimo:
            tope2 = str(i)
            break
    
    imagen.close()
    return [tope1,tope2]

def contraste(ruta,topes):
    imagen = Image.open(ruta)
    pixels = imagen.load()

    anchura = imagen.width
    altura= imagen.height
    maximo = int(topes[1])
    minimo = int(topes[0])
    pedestal = minimo
    multiplo = 255/(maximo-minimo)
    for x in range(0,anchura):
        for y in range(0,altura):
            color = imagen.getpixel((x,y))
            pixels[x,y] = (
                round((color[0]-pedestal)*multiplo),
                round((color[1]-pedestal)*multiplo),
                round((color[2]-pedestal)*multiplo)
                )
    
    imagen.save(ruta)
    imagen.close()
    
contraste("foto.jpg",histograma("foto.jpg"))




