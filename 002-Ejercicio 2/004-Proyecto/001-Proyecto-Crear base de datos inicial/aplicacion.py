import sqlite3 as lite
import tkinter as tk

# Preparo la base de datos en el caso de que no exista
mibd = "aplicacion.sqlite3"
conexion = lite.connect(mibd)
conexion.execute('''CREATE TABLE IF NOT EXISTS clientes  (
                        identificador INTEGER,
                        nombre TEXT,
                        apellidos TEXT,
                        email TEXT,
                        telefono TEXT,
                        PRIMARY KEY("identificador" AUTOINCREMENT)
                    )''')
conexion.commit()
conexion.execute('''CREATE TABLE IF NOT EXISTS productos  (
                        identificador INTEGER,
                        nombre TEXT,
                        descripcion TEXT,
                        precio TEXT,
                        peso TEXT,
                        direccioncompleta TEXT,
                        PRIMARY KEY("identificador" AUTOINCREMENT)
                    )''')
conexion.commit()
conexion.execute('''CREATE TABLE IF NOT EXISTS pedidos  (
                        identificador INTEGER,
                        numero TEXT,
                        fecha TEXT,
                        FK_clientes_nombre TEXT,
                        PRIMARY KEY("identificador" AUTOINCREMENT)
                    )''')
conexion.commit()
conexion.execute('''CREATE TABLE IF NOT EXISTS lineaspedido  (
                        identificador INTEGER,
                        FK_pedidos_numero TEXT,
                        FK_productos_nombre TEXT,
                        cantidad TEXT,
                        PRIMARY KEY("identificador" AUTOINCREMENT)
                    )''')
conexion.commit()




