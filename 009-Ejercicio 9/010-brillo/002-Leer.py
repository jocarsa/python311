from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()

anchura = imagen.width
altura= imagen.height
desfase = 127
for x in range(0,anchura):
    for y in range(0,altura):
        color = imagen.getpixel((x,y))
        pixels[x,y] = (color[0]+desfase,color[1]+desfase,color[2]+desfase)

imagen.save("modificado.jpg")

imagen.close()
