#pip install lxml
#pip install bs4
import lxml
from bs4 import BeautifulSoup

archivo = open("001-menu.xml","r")
datos = archivo.read()

xml = BeautifulSoup(datos, "xml")
print(xml)
menus = xml.find_all('menu')
print(menus)
comandos = xml.find_all('comando')
print(comandos)

