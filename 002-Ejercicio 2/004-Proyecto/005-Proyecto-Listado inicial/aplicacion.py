import sqlite3 as lite
import tkinter as tk
from tkinter import ttk

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
def editaTabla(tabla):
    print("Voy a editar la tabla:"+tabla)

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
cursor = conexion.cursor()
cursor.execute('''
SELECT name FROM sqlite_master WHERE type='table';
''')
datos = cursor.fetchall()
for registro in datos:
    print(registro)
    editar.add_command(
        label=str(registro[0]),
        command=lambda r=registro[0]: editaTabla(str(r))
    )

marco = tk.Frame()
marco.pack

columnas = ('nombre', 'apellidos', 'email')
arbol = ttk.Treeview(raiz, columns=columnas, show='headings')
arbol.pack()
arbol.heading('nombre', text='Nombre del cliente')
arbol.heading('apellidos', text='Apellidos del cliente')
arbol.heading('email', text='Correo electrónico del cliente')
arbol.insert('', tk.END, values=['Jose Vicente','Carratalá Sanchis','info@josevicentecarratala.com'])
raiz.mainloop()


raiz.mainloop()


