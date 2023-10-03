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





