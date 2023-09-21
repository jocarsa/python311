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

def prueba():
    print("ok prueba")

#Ventana TKinter
raiz = tk.Tk()

# Menu

mimenu = tk.Menu()
raiz.config(menu=mimenu)

archivo = tk.Menu(mimenu, tearoff=False)
editar = tk.Menu(mimenu, tearoff=False)
ayuda = tk.Menu(mimenu, tearoff=False)
mimenu.add_cascade(menu=archivo, label="Archivo")
mimenu.add_cascade(menu=editar, label="Editar")
mimenu.add_cascade(menu=ayuda, label="Ayuda")

editar.add_command(
    label="Clientes",
    command=prueba
)
editar.add_command(
    label="Productos",
    command=prueba
)
editar.add_command(
    label="Pedidos",
    command=prueba
)
editar.add_command(
    label="Lineas de pedidos",
    command=prueba
)

raiz.mainloop()


