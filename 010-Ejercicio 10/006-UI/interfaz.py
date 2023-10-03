import tkinter as tk

raiz = tk.Tk()

def seleccionaCarpeta():
    print("vamos a por ello")

def ejecutar():
    print("ejecutamos")

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
