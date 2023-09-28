from PIL import Image

image = Image.open('estrellas.png')

for x1 in range(0,8192,64):
    for y1 in range(0,8192,64):
        bloque = image.crop((x1, y1, x1+64, y1+64))

        width, height = bloque.size

        for y in range(height):
            for x in range(width):      
                pixel = bloque.getpixel((x, y))
                # print(f"Pixel at ({x}, {y}): R={pixel[0]}, G={pixel[1]}, B={pixel[2]}")
                if pixel[0] == 255:
                    print("estrella encontrada en "+str(x+x1)+","+str(y+y1))
                    
image.close()
