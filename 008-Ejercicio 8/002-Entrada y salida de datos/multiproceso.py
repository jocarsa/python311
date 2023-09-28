import multiprocessing

def trabajador(arg, result_dict):
    numero = 1.000000012
    result = []
    for i in range(0, 100000000):
        i *= 1.000000012
    result.append(i)
    result_dict[arg] = result

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        result_dict = manager.dict()

        piscina = multiprocessing.Pool(processes=6)

        # Use starmap to pass both arg and result_dict to the worker function
        args = [(i, result_dict) for i in range(10)]
        piscina.starmap(trabajador, args)
        piscina.close()
        print("he cerrado un proceso")
        piscina.join()
        print("han finalizado los procesos")

        # Retrieve results from the result_dict
        results = [result_dict[i] for i in range(10)]
        print("Results:", results)
