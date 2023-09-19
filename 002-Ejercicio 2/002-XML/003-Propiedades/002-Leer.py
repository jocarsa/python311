#pip install lxml
#pip install bs4
import lxml
from bs4 import BeautifulSoup

archivo = open("001-menu.xml","r")
datos = archivo.read()

xml = BeautifulSoup(datos, "xml")
menu = xml.find_all('menu')
for elemento in menu:
    print("tengo un elemento que es:")
    print(elemento)
    subxml = BeautifulSoup(str(elemento), "xml")
    comando = subxml.find_all('comando')
    for subelemento in comando:
        print("Tengo un comando:")
        print(subelemento)



