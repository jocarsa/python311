import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

marco = tk.Frame()
marco.pack

columnas = ('nombre', 'apellidos', 'email')
arbol = ttk.Treeview(raiz, columns=columnas, show='headings')
arbol.pack()
arbol.heading('nombre', text='Nombre del cliente')
arbol.heading('apellidos', text='Apellidos del cliente')
arbol.heading('email', text='Correo electrónico del cliente')
arbol.insert('', tk.END, values=['Jose Vicente','Carratalá Sanchis','info@josevicentecarratala.com'])
raiz.mainloop()



