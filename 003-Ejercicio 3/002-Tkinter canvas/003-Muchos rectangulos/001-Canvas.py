import tkinter as tk
import random

raiz = tk.Tk()

raiz.geometry("512x512")

lienzo = tk.Canvas(raiz, width=512, height=512)
lienzo.pack()
for i in range(0,500):
    x = random.randint(0,512)
    y = random.randint(0,512)
    lienzo.create_rectangle(x,y,x+10,y+10,fill="#0000ff")

raiz.mainloop()

    
