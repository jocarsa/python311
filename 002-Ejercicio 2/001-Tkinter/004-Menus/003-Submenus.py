import tkinter as tk

def nuevoArchivo():
    print("Vamos a crear un nuevo archivo")

raiz = tk.Tk()
raiz.title("Super programa")


mimenu = tk.Menu()
raiz.config(menu=mimenu)

archivo = tk.Menu(mimenu, tearoff=False)
editar = tk.Menu(mimenu, tearoff=False)
ayuda = tk.Menu(mimenu, tearoff=False)
mimenu.add_cascade(menu=archivo, label="Archivo")
mimenu.add_cascade(menu=editar, label="Editar")
mimenu.add_cascade(menu=ayuda, label="Ayuda")

archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=nuevoArchivo
)
archivo.add_command(
    label="Abrir",
    accelerator="Ctrl+O",
    command=nuevoArchivo
)
archivo.add_command(
    label="Guardar",
    accelerator="Ctrl+S",
    command=nuevoArchivo
)


raiz.mainloop()

