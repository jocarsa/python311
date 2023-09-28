# pip install pandas openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Check for command-line argument
if len(sys.argv) < 2:
    print("Es necesario introducir el archivo")
    sys.exit(1)

archivo = sys.argv[1]
titulo = os.path.splitext(os.path.basename(archivo))[0]
contenido = pd.read_excel(archivo)

output_folder = "graficas/"
os.makedirs(output_folder, exist_ok=True)

with open(f"{output_folder}{titulo}.html", "w") as informe:
    informe.write('''
        <!doctype html>
        <html>
        <head>
        </head>
        <body>
    ''')

    for columna_nombre, columna in contenido.items():
        informe.write(f"<h1>{columna_nombre}</h1>")
        value_counts = columna.value_counts()

        if len(value_counts) > 1:
            # Pie Chart
            try:
                informe.write("<h2>Gráfico de tarta</h2>")
                plt.figure(figsize=(6, 6))
                plt.pie(value_counts, labels=value_counts.index, startangle=90)
                plt.title(columna_nombre)
                plt.axis('equal')
                plt.savefig(f"{output_folder}{titulo}-tarta-{columna_nombre}.png")
                informe.write(f"<img src='{titulo}-tarta-{columna_nombre}.png'>")
                plt.close()
            except Exception as e:
                print(f"Error creating pie chart for {columna_nombre}: {e}")

            # Bar Chart
            try:
                informe.write("<h2>Gráfico de barras</h2>")
                plt.figure(figsize=(8, 5))
                plt.bar(value_counts.index, value_counts.values, color='skyblue')
                plt.xlabel(columna_nombre)
                plt.ylabel('Valor')
                plt.title(columna_nombre)
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.savefig(f"{output_folder}{titulo}-barras-{columna_nombre}.png")
                informe.write(f"<img src='{titulo}-barras-{columna_nombre}.png'>")
                plt.close()
            except Exception as e:
                print(f"Error creating bar chart for {columna_nombre}: {e}")

    informe.write('''
        </body>
        </html>
    ''')

print("Report generated successfully.")
