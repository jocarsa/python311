import multiprocessing

def trabajador(arg):
    numero = 1.000000012
    for i in range(0,100000000):
        i *= 1.000000012
    

if __name__ == "__main__":
    piscina = multiprocessing.Pool(processes=6)
    resultado = piscina.map(trabajador, range(10))
    piscina.close()
    print("he cerrado un proceso")
    piscina.join()
    print("han finalizado los procesos")
