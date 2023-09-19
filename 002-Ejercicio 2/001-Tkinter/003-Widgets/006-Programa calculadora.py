import tkinter as tk

def pulsaBoton():
    print("Has pulsado el boton")
    contenido = int(varcampo.get())
    contenido2 = int(varcampo2.get())
    resultado = contenido + contenido2
    print("El resultado de la suma es:"+str(resultado))

raiz = tk.Tk()
raiz.geometry("600x600+0+0")
raiz.title("Super programa")
icono = tk.PhotoImage(file="icono.png")
raiz.iconphoto(True, icono)

varcampo = tk.StringVar()
varcampo2 = tk.StringVar()

etiqueta = tk.Label(text="Programa agenda por Jose Vicente Carratala")
etiqueta.grid(row=0,column=0)

entrada = tk.Entry(textvariable=varcampo)
entrada.grid(row=1,column=0)

entrada2 = tk.Entry(textvariable=varcampo2)
entrada2.grid(row=2,column=0)

boton = tk.Button(text="Pulsame",command=pulsaBoton)
boton.grid(row=3,column=0)

raiz.mainloop()

