from PIL import Image
imagen = Image.open('josevicente.jpg') 
pixel = imagen.getpixel((0,0))
print(pixel)
