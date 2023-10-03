# Programa agenda por Jose Vicente Carratalá Sanchis
from os import system
import json

from modulos.funciones import *


archivo = open("agenda.txt","r")
agenda = json.load(archivo)

def menu():
    imprimeMenu()
    opcion = input()
    print("Has seleccionado la opcion: "+opcion)
    if(opcion == "1"):
        verRegistros()
    elif(opcion == "2"):
        buscaRegistro()
    elif(opcion == "3"):
        creaRegistro()
    elif(opcion == "4"):
        modificaRegistro()
    elif(opcion == "5"):
        eliminaRegistro()
    elif(opcion == "6"):
        salir()
        
    input("Pulsa una tecla para continuar....")
    menu()
menu()
