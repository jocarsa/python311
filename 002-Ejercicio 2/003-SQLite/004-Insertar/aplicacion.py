import sqlite3

mibd = "aplicacion.sqlite3"

conexion = sqlite3.connect(mibd)

conexion.execute('''
    INSERT INTO clientes
    VALUES (
    NULL,
    'Jose Vicente',
    'Carratalá Sanchis',
    'info@josevicentecarratala.com',
    '12345'
    )
''')
conexion.commit()

conexion.close()
