from PIL import Image

def contraste(ruta):
    imagen = Image.open(ruta)
    pixels = imagen.load()

    anchura = imagen.width
    altura= imagen.height
    maximo = 0
    minimo = 10000000
    for x in range(0,anchura):
        for y in range(0,altura):
            color = imagen.getpixel((x,y))
            gris = round((color[0]+color[1]+color[2])/3)
            if gris > maximo:
                maximo = gris
            if gris < minimo:
                minimo = gris
    print("maximo:"+str(maximo))
    print("mínimo:"+str(minimo))
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
    
contraste("foto.jpg")


