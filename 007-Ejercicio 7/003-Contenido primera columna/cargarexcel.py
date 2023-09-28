#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl

archivo = "registros.xlsx"

contenido = pd.read_excel(archivo)

primeracolumna = contenido.iloc[:, 0]
print(primeracolumna)

primeracolumnalista=  primeracolumna.values.tolist()

print(primeracolumnalista)


