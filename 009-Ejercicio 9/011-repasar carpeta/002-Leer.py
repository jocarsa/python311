from PIL import Image
import os
import sys


for root, dirnames, filenames in os.walk("../fotos"):
    for archivo in filenames:
        try:
            rutacompleta = os.path.join(root, archivo)
            imagen = Image.open(rutacompleta)
            pixels = imagen.load()

            anchura = imagen.width
            altura= imagen.height
            for x in range(0,anchura):
                for y in range(0,altura):
                    color = imagen.getpixel((x,y))
                    pixels[x,y] = (
                        color[0]*2,
                        color[1]*2,
                        color[2]*2
                        )
            imagen.save(rutacompleta)
            imagen.close()
        except:
            print("No es una imagen")
