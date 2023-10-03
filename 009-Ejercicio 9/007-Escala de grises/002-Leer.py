from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height

for x in range(0,anchura):
    for y in range(0,altura):
        color = imagen.getpixel((x,y))
        gris = round((color[0]+color[1]+color[2])/3)
        pixels[x,y] = (gris,gris,gris)

imagen.save("modificado.jpg")

imagen.close()
