from PIL import Image

image = Image.open('estrellas.png')

def busca(imagen,x,y):
    bloque = imagen.crop((x, y, x+64, y+64))
    width, height = bloque.size
    for y in range(height):
        for x in range(width):      
            pixel = bloque.getpixel((x, y))
            # print(f"Pixel at ({x}, {y}): R={pixel[0]}, G={pixel[1]}, B={pixel[2]}")
            if pixel[0] == 255:
                print("estrella encontrada en "+str(x+x1)+","+str(y+y1))


for x1 in range(0,8192,64):
    for y1 in range(0,8192,64):
        busca(image,x1,y1)
                            
image.close()
