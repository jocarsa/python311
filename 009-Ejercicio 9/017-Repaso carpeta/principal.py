from histograma import histograma
from contraste import contraste
import os

for root, dirnames, filenames in os.walk("../fotos"):
    for archivo in filenames:
        try:
            rutacompleta = os.path.join(root, archivo)
            contraste(rutacompleta,histograma(rutacompleta))
        except:
            print("error")




