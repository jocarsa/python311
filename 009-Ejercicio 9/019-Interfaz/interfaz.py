import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import subprocess

raiz = tk.Tk()

style = ttk.Style()
style.theme_use("xpnative")

micarpeta = ""

def seleccionaCarpeta():
    global micarpeta
    global nombredecarpeta
    print("Has seleccionado una carpeta")
    carpeta = filedialog.askdirectory()
    micarpeta = carpeta
    print("Has seleccionado la carpeta:",carpeta)
    nombredecarpeta.config(text=carpeta)

def ejecutar():
    print("ejecutamos")
    cmd = ["python", "principal.py", micarpeta]
    subprocess.check_output(cmd, universal_newlines=True)


marco = tk.Frame(raiz,width=300,height=300,padx=20,pady=20)
marco.pack_propagate(False)
marco.pack()

tk.Label(marco,text="Introduce la carpeta").pack()
tk.Button(marco,text="Selecciona",command=seleccionaCarpeta).pack()
nombredecarpeta = tk.Label(marco,text=".")
nombredecarpeta.pack()
tk.Button(marco,text="Vamos allá",command=ejecutar).pack()

raiz.mainloop()
