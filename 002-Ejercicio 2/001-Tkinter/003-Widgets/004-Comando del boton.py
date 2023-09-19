import tkinter as tk

def pulsaBoton():
    print("Has pulsado el boton")

raiz = tk.Tk()
raiz.geometry("600x600+0+0")
raiz.title("Super programa")
icono = tk.PhotoImage(file="icono.png")
raiz.iconphoto(True, icono)

etiqueta = tk.Label(text="Programa agenda por Jose Vicente Carratala")
etiqueta.grid(row=0,column=0)

entrada = tk.Entry()
entrada.grid(row=1,column=0)

boton = tk.Button(text="Pulsame",command=pulsaBoton)
boton.grid(row=2,column=0)

raiz.mainloop()

