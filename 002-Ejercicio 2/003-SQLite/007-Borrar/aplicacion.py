import sqlite3

conexion = sqlite3.connect("aplicacion.sqlite3")
cursor = conexion.cursor()
cursor.execute('''
DELETE FROM clientes
WHERE nombre = 'Juan';
''')

conexion.commit()
conexion.close()
