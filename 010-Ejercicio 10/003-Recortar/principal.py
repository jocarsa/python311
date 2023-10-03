import os
from PIL import Image, ImageFilter

def reescala(carpeta,ancho,alto):
    for root, dirnames, filenames in os.walk(carpeta):
        for archivo in filenames:
            try:
                rutacompleta = os.path.join(root, archivo)
                imagen = Image.open(rutacompleta)
                anchura = imagen.width
                altura= imagen.height
                if anchura < altura:
                    manda = "anchura"
                else:
                    manda = "altura"
                
                if manda == "anchura":
                    proporcion = altura/anchura
                    reescalado = imagen.resize(
                        (ancho,round(ancho*proporcion)),
                        Image.Resampling.LANCZOS
                        )
                else:
                    proporcion = anchura/altura
                    reescalado = imagen.resize(
                        (round(alto*proporcion),alto),
                        Image.Resampling.LANCZOS
                        )
                reescalado.save(rutacompleta)
            except:
                print("error")

reescala("../fotos",200,200)




