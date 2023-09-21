import tkinter as tk
import random
import math

class Ser:
    def __init__(self):
        self.posx = random.randint(0,512)
        self.posy = random.randint(0,512)
        self.direccion = random.randint(0,360)

class Persona(Ser):
    def __init__(self):
        super().__init__()
        self.nombre = ""
        
    def dimeNombre(self):
        return self.nombre
    def tomaNombre(self,nuevonombre):
        self.nombre = nuevonombre
    def dibuja(self):
        lienzo.create_rectangle(
            self.posx,
            self.posy,
            self.posx+10,
            self.posy+10,
            fill="blue"
            )
    def mueve(self):
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)

raiz = tk.Tk()

raiz.geometry("512x512")

lienzo = tk.Canvas(raiz, width=512, height=512)
lienzo.pack()

numeropersonas = 100
personas = []
for i in range(0,numeropersonas):
    personas.append(Persona())

def bucle():
    for persona in personas:
        persona.mueve()
        persona.dibuja()
    #print("estas en el bucle")
    raiz.after(100,bucle)

bucle()

raiz.mainloop()















    
