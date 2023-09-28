#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl
import matplotlib.pyplot as plt


archivo = "registros.xlsx"

contenido = pd.read_excel(archivo)
primeracolumna = contenido.iloc[:, 0]
primeracolumnalista=  primeracolumna.values.tolist()

valores = {}

for registro in primeracolumnalista:
    if registro in valores:
        valores[registro] += 1
    else:
        valores[registro] = 1

ordenado = sorted(valores.items(), key=lambda x: x[1], reverse=True)

for clave, valor in ordenado:
    print(f"{clave}: {valor}")

print(ordenado)

etiquetas = [item[0] for item in ordenado]
valores = [item[1] for item in ordenado]

plt.figure(figsize=(6, 6)) 
plt.pie(valores, labels=etiquetas, startangle=90)

plt.title('Año')

plt.axis('equal')  
plt.show()
