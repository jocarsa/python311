import tkinter as tk
from tkinter import filedialog

def seleccionaCarpeta():
    print("Has seleccionado una carpeta")
    carpeta = filedialog.askdirectory()
    print("Has seleccionado la carpeta:",carpeta)

def buscador():
    print("Ahora voy a buscar")
    print("Voy a buscar:",termino_busqueda.get())

raiz = tk.Tk()

termino_busqueda = tk.StringVar()

marco = tk.Frame(padx=50,pady=50)
marco.pack()

tk.Label(marco,text="Introduce la carpeta").pack()
tk.Button(marco,text="Selecciona",command=seleccionaCarpeta).pack()
tk.Label(marco,text="Introduce la palabra a buscar").pack()
tk.Entry(marco,textvariable=termino_busqueda).pack()
tk.Button(marco,text="¡Busca!",command=buscador).pack()

raiz.mainloop()
