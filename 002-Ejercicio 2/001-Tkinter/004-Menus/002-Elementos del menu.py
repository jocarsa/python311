import tkinter as tk


raiz = tk.Tk()
raiz.title("Super programa")


mimenu = tk.Menu()
raiz.config(menu=mimenu)

archivo = tk.Menu(mimenu, tearoff=False)
mimenu.add_cascade(menu=archivo, label="Archivo")
mimenu.add_cascade(menu=archivo, label="Editar")
mimenu.add_cascade(menu=archivo, label="Ayuda")

raiz.mainloop()

