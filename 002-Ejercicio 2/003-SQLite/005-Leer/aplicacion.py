import sqlite3

conexion = sqlite3.connect("aplicacion.sqlite3")
cursor = conexion.cursor()
cursor.execute('''
SELECT * FROM clientes;
''')

datos = cursor.fetchall()

print(datos)

for registro in datos:
    print(registro)
    for columna in registro:
        print(columna)


conexion.commit()
