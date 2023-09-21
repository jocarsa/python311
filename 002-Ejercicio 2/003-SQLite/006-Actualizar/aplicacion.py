import sqlite3

conexion = sqlite3.connect("aplicacion.sqlite3")
cursor = conexion.cursor()
cursor.execute('''
UPDATE clientes
SET telefono = 567890
WHERE nombre = 'Juan';
''')

conexion.commit()
conexion.close()
