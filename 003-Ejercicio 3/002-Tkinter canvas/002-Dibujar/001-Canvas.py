import tkinter as tk

raiz = tk.Tk()

raiz.geometry("512x512")

lienzo = tk.Canvas()
lienzo.pack()

lienzo.create_rectangle(50,50,200,200,fill="#0000ff")

raiz.mainloop()

    
