from PIL import Image
import multiprocessing


def busca(args):
    imagen, x, y, tamanio = args
    bloque = imagen.crop((x, y, x+tamanio, y+tamanio))
    width, height = bloque.size
    for y1 in range(height):
        for x1 in range(width):
          
            pixel = bloque.getpixel((x1, y1))
            if pixel[0] == 255:
                archivo = open("resultado.txt","w")
                archivo.write("estrella encontrada en: "+str(x+x1)+","+str(y+y1))
                archivo.close()
def main():
    image = Image.open('estrellas.png')
    tamanio = 2048
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

if __name__ == "__main__":
    main()
