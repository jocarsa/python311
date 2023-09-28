from PIL import Image

image = Image.open('estrellas.png') 
width, height = image.size

for y in range(height):
    for x in range(width):      
        pixel = image.getpixel((x, y))
        # print(f"Pixel at ({x}, {y}): R={pixel[0]}, G={pixel[1]}, B={pixel[2]}")
        if pixel[0] == 255:
            print("estrella encontrada en "+str(x)+","+str(y))
            
image.close()
