#pip install pandas
import pandas as pd
#pip install openpyxl
import openpyxl

excel_file_path = "registros.xlsx"

df = pd.read_excel(excel_file_path)

print(df.head())
