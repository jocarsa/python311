from PIL import Image
import multiprocessing
import time
import PIL

PIL.Image.MAX_IMAGE_PIXELS = 933120000

def busca(args):
    imagen, x, y, tamanio = args
    bloque = imagen.crop((x, y, x+tamanio, y+tamanio))
    width, height = bloque.size
    for y1 in range(height):
        for x1 in range(width):
            pixel = bloque.getpixel((x1, y1))
            if pixel[0] == 255:
                archivo = open("resultado.txt", "a")  # Use 'a' to append to the file
                archivo.write("estrella encontrada en: " + str(x + x1) + "," + str(y + y1) + "\n")
                archivo.close()

def main():
    tamanios = [4,8,16,32,64,128,256,512,1024,2048,4192,8192]
    for mitamanio in tamanios:
        start_time = time.time()  # Record the start time
        image = Image.open('estrellas2.png')
        tamanio = mitamanio
        pool = multiprocessing.Pool()  # Create a pool of processes

        args_list = []
        for x1 in range(0, 8192, tamanio):
            for y1 in range(0, 8192, tamanio):
                args_list.append((image, x1, y1, tamanio))

        # Use the pool to process the image blocks in parallel
        pool.map(busca, args_list)

        pool.close()
        pool.join()
        image.close()

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print("Total time elapsed: {:.2f} seconds".format(elapsed_time)+" en tamaño:"+str(tamanio))

if __name__ == "__main__":
    main()
