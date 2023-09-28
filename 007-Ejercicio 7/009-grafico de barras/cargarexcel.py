#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl
import matplotlib.pyplot as plt


archivo = "registros.xlsx"

contenido = pd.read_excel(archivo)

numero_de_columnas = len(contenido.columns)

for i in range(0,numero_de_columnas):
    primeracolumna_nombre = contenido.columns[i]
    primeracolumna = contenido.iloc[:, i]
    primeracolumnalista=  primeracolumna.values.tolist()

    valores = {}

    for registro in primeracolumnalista:
        if registro in valores:
            valores[registro] += 1
        else:
            valores[registro] = 1

    ordenado = sorted(valores.items(), key=lambda x: x[1], reverse=True)
    etiquetas = [item[0] for item in ordenado]
    valores = [item[1] for item in ordenado]
    try:
        plt.figure(figsize=(6, 6)) 
        plt.pie(valores, labels=etiquetas, startangle=90)
        plt.title(primeracolumna_nombre)
        plt.axis('equal')  
        plt.savefig("graficas/tarta-"+primeracolumna_nombre)
        plt.close()
    except:
        pass
    try:
        plt.figure(figsize=(8, 5))
        plt.bar(etiquetas, valores, color='skyblue')
        plt.xlabel(primeracolumna_nombre)
        plt.ylabel('Valor')
        plt.title(primeracolumna_nombre)
        plt.savefig("graficas/barras-"+primeracolumna_nombre)
        plt.close()
    except:
        pass
