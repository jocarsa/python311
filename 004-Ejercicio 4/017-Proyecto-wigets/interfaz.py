import tkinter as tk

raiz = tk.Tk()

marco = tk.Frame(padx=50,pady=50)
marco.pack()

tk.Label(marco,text="Introduce la carpeta").pack()
tk.Button(marco,text="Selecciona").pack()

raiz.mainloop()
