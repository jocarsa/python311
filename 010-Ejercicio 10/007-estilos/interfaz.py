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
    print("Has seleccionado una carpeta")
    carpeta = filedialog.askdirectory()
    micarpeta = carpeta
    print("Has seleccionado la carpeta:",carpeta)

def ejecutar():
    print("ejecutamos")
    cmd = ["python", "principal.py", micarpeta, anchura.get(), altura.get()]
    subprocess.check_output(cmd, universal_newlines=True)

anchura = tk.StringVar()
altura = tk.StringVar()

marco = tk.Frame(raiz,width=300,height=300,padx=20,pady=20)
marco.pack_propagate(False)
marco.pack()

tk.Label(marco,text="Introduce la carpeta").pack()
tk.Button(marco,text="Selecciona",command=seleccionaCarpeta).pack()
tk.Label(marco,text="Introduce la anchura").pack()
tk.Entry(marco,textvariable=anchura).pack()
tk.Label(marco,text="Introduce la altura").pack()
tk.Entry(marco,textvariable=altura).pack()
tk.Button(marco,text="Vamos allá",command=ejecutar).pack()

raiz.mainloop()
