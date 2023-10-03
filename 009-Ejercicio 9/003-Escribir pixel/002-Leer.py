from PIL import Image

imagen = Image.open("josevicente.jpg")
pixels = imagen.load()
pixels[0,0] = (0,255,0,255)

imagen.save("modificado.png")

imagen.close()
