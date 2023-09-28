from PIL import Image

image = Image.open('estrellas.png')

def busca(imagen,x,y,tamanio):
    bloque = imagen.crop((x, y, x+tamanio, y+tamanio))
    width, height = bloque.size
    for y in range(height):
        for x in range(width):      
            pixel = bloque.getpixel((x, y))
            # print(f"Pixel at ({x}, {y}): R={pixel[0]}, G={pixel[1]}, B={pixel[2]}")
            if pixel[0] == 255:
                print("estrella encontrada en "+str(x+x1)+","+str(y+y1))

tamanio = 512

for x1 in range(0,8192,tamanio):
    for y1 in range(0,8192,tamanio):
        busca(image,x1,y1,tamanio)
                            
image.close()
