import os
from PIL import Image, ImageFilter

for root, dirnames, filenames in os.walk("../fotos"):
    for archivo in filenames:
        #try:
            rutacompleta = os.path.join(root, archivo)
            imagen = Image.open(rutacompleta)
            reescalado = imagen.resize((200,200), Image.Resampling.LANCZOS)
            reescalado.save(rutacompleta)
        #except:
           # print("error")




