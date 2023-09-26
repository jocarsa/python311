import tkinter as tk
from tkinter import filedialog

def seleccionaCarpeta():
    print("Has seleccionado una carpeta")
    carpeta = filedialog.askdirectory()
    print("Has seleccionado la carpeta:",carpeta)

raiz = tk.Tk()

marco = tk.Frame(padx=50,pady=50)
marco.pack()

tk.Label(marco,text="Introduce la carpeta").pack()
tk.Button(marco,text="Selecciona",command=seleccionaCarpeta).pack()

raiz.mainloop()
