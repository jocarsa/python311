#pip install pandas
import pandas as pd

excel_file_path = "registros.xlsx"

df = pd.read_excel(excel_file_path)

print(df.head())
