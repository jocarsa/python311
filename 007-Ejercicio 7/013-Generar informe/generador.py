import tkinter as tk
from tkinter import filedialog
import os
import subprocess

micarpeta = ""

def seleccionaCarpeta():
    global micarpeta
    print("Has seleccionado una carpeta")
    carpeta = filedialog.askopenfilename()
    micarpeta = carpeta
    print("Has seleccionado la carpeta:",carpeta)

def buscador():
    global cajatexto
    cmd = ["python", "cargarexcel.py", micarpeta]
    salida = subprocess.check_output(cmd, universal_newlines=True)



raiz = tk.Tk()

marco = tk.Frame(padx=50,pady=50)
marco.pack()

tk.Label(marco,text="Introduce el archivo").pack()
tk.Button(marco,text="Selecciona",command=seleccionaCarpeta).pack()
tk.Button(marco,text="¡Genera!",command=buscador).pack()


raiz.mainloop()
