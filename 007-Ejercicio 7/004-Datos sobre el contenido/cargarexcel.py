#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl

archivo = "registros.xlsx"

contenido = pd.read_excel(archivo)
primeracolumna = contenido.iloc[:, 0]
primeracolumnalista=  primeracolumna.values.tolist()

for registro in primeracolumnalista:
    print(registro)


