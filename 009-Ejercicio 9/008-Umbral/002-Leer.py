from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height
umbral = 127
for x in range(0,anchura):
    for y in range(0,altura):
        color = imagen.getpixel((x,y))
        gris = round((color[0]+color[1]+color[2])/3)
        if gris < umbral:
            componente = 0
        else:
            componente = 255
        pixels[x,y] = (componente,componente,componente)

imagen.save("modificado.jpg")

imagen.close()
