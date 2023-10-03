from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height

for x in range(0,anchura):
    for y in range(0,altura):
        pixels[x,y] = (0,255,0)

imagen.save("modificado.jpg")

imagen.close()
