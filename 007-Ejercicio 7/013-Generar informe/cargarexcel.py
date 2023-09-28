#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl
import matplotlib.pyplot as plt
import os
import sys

try:
    archivo = sys.argv[1]
except:
    print("Es necesario introducir el archivo")
    sys.exit(1)



titulo = archivo.split("/")[-1].split(".")[0]
contenido = pd.read_excel(archivo)

informe = open("graficas/"+titulo+".html","w")
informe.write('''
    <!doctype html>
    <html>
    <head>
    </head>
    <body>
''')

numero_de_columnas = len(contenido.columns)

for i in range(0,numero_de_columnas):
    primeracolumna_nombre = contenido.columns[i]
    primeracolumna = contenido.iloc[:, i]
    primeracolumnalista=  primeracolumna.values.tolist()
    informe.write("<h1>"+primeracolumna_nombre+"</h1>")
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
        informe.write("<h2>Gráfico de tarta</h2>")
        plt.figure(figsize=(6, 6)) 
        plt.pie(valores, labels=etiquetas, startangle=90)
        plt.title(primeracolumna_nombre)
        plt.axis('equal')  
        plt.savefig("graficas/"+titulo+"-tarta-"+primeracolumna_nombre)
        informe.write("<img src='"+titulo+"-tarta-"+primeracolumna_nombre+".png'>")
        plt.close()
    except:
        pass
    try:
        informe.write("<h2>Gráfico de barras</h2>")
        plt.figure(figsize=(8, 5))
        plt.bar(etiquetas, valores, color='skyblue')
        plt.xlabel(primeracolumna_nombre)
        plt.ylabel('Valor')
        plt.title(primeracolumna_nombre)
        plt.savefig("graficas/"+titulo+"-barras-"+primeracolumna_nombre)
        informe.write("<img src='"+titulo+"-barras-"+primeracolumna_nombre+".png'>")
        plt.close()
    except:
        pass

informe.close()
