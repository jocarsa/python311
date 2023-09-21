import tkinter as tk
import random
import math
import json

nombres = [
    "María",
    "Juan",
    "Ana",
    "Carlos",
    "Luis",
    "Elena",
    "José",
    "Sofía",
    "Miguel",
    "Lucía",
    "Pedro",
    "Isabel",
    "Alejandro",
    "Laura",
    "Javier",
    "Carmen",
    "David",
    "Patricia",
    "Daniel",
    "Eva",
    "Francisco",
    "Rosa",
    "Antonio",
    "Beatriz",
]

class Ser:
    def __init__(self):
        self.posx = random.randint(0,512)
        self.posy = random.randint(0,512)
        self.direccion = random.randint(0,360)

class Persona(Ser):
    def __init__(self):
        super().__init__()
        self.nombre = nombres[random.randint(0,len(nombres)-1)]
        self.rojo = random.randint(0,255)
        self.verde = random.randint(0,255)
        self.azul = random.randint(0,255)
        
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
            fill="#"+format(self.rojo, '02x')+format(self.verde, '02x')+format(self.azul, '02x')
            )
        lienzo.create_text(
            self.posx,
            self.posy-5,
            text=self.nombre,
            font=("Helvetica", 10)
            )
        
        self.mueve()
    def mueve(self):
        self.rebota()
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
    def rebota(self):
        if self.posx < 0 or self.posx > 512 or self.posy < 0 or self.posy > 512:
            self.direccion += math.pi

def cierre():
    print("vamos a cerrar")
    archivo = open("memoria.txt","w")
    for persona in personas:
        propiedades = vars(persona)
        cadenajson = json.dumps(propiedades)
        archivo.write(cadenajson+"\n")
    archivo.close()
    raiz.destroy()

raiz = tk.Tk()

raiz.geometry("512x512")

lienzo = tk.Canvas(raiz, width=512, height=512)
lienzo.pack()

numeropersonas = 100
personas = []
for i in range(0,numeropersonas):
    personas.append(Persona())

def bucle():
    lienzo.delete('all')
    for persona in personas:
        persona.dibuja()
    #print("estas en el bucle")
    raiz.after(100,bucle)

bucle()
raiz.protocol("WM_DELETE_WINDOW", cierre)
raiz.mainloop()















    
