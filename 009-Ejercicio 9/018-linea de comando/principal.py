from histograma import histograma
from contraste import contraste
import os
import sys

nombrecarpeta = sys.argv[1]

for root, dirnames, filenames in os.walk(nombrecarpeta):
    for archivo in filenames:
        try:
            rutacompleta = os.path.join(root, archivo)
            contraste(rutacompleta,histograma(rutacompleta))
        except:
            print("error")




