import sqlite3

mibd = "aplicacion.sqlite3"

conexion = sqlite3.connect(mibd)

conexion.execute('''CREATE TABLE IF NOT EXISTS clientes  (
                        identificador INTEGER,
                        nombre TEXT,
                        apellidos TEXT,
                        email TEXT,
                        telefono TEXT,
                        PRIMARY KEY("identificador" AUTOINCREMENT)
                    )''')
