from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height

for x in range(0,anchura):
    for y in range(0,altura):
        color = imagen.getpixel((x,y))
        rojo = 255-color[0]
        verde = 255-color[0]
        azul = 255-color[0]
        pixels[x,y] = (rojo,verde,azul)

imagen.save("modificado.jpg")

imagen.close()
