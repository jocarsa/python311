from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height
umbral = 127
for x in range(0,anchura):
    for y in range(0,altura):
        color = imagen.getpixel((x,y))
        pixels[x,y] = (color[0]*2,color[1]*2,color[2]*2)

imagen.save("modificado.jpg")

imagen.close()
