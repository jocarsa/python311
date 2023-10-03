# Programa agenda por Jose Vicente Carratalá Sanchis
from os import system
import json
agenda = []

archivo = open("agenda.txt","r")
agenda = json.load(archivo)

def imprimeMenu():
    system('cls')
    print('''
    Programa Agenda
    (c) 2023 Jose Vicente Carratalá Sanchis
    1.-Ver todos los registros
    2.-Buscar un registro
    3.-Crear un nuevo registro
    4.-Modificar un registro
    5.-Eliminar un registro
    6.-Salir
    -Selecciona una opcion:
    ''')
def verRegistros():
    system('cls')
    print("Vamos a mostrar todos los registros")
    print("id \t\t nombre \t\t email \t\t teléfono")
    print("----------------------------------------")
    contador = 0
    for registro in agenda:
        print(contador, end="")
        print("\t\t", end="")
        print(registro['nombre'], end="")
        print("\t\t", end="")
        print(registro['email'], end="")
        print("\t\t", end="")
        print(registro['telefono'])
        contador += 1
def buscaRegistro():
    system('cls')
    print("Vamos a buscar un registro")
    nombre = input("Introduce el nombre de la persona: ")
    print("id \t\t nombre \t\t email \t\t teléfono")
    print("----------------------------------------")
    contador = 0
    for registro in agenda:
        if registro['nombre'] == nombre:
            print(contador, end="")
            print("\t\t", end="")
            print(registro['nombre'], end="")
            print("\t\t", end="")
            print(registro['email'], end="")
            print("\t\t", end="")
            print(registro['telefono'])
        contador += 1
def creaRegistro():
    system('cls')
    print("Vamos a insertar un registro")
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el teléfono: ")
    agenda.append({"nombre":nombre,"email":email,"telefono":telefono})
def modificaRegistro():
    system('cls')
    print("Vamos a modificar un registro")
    identificador = int(input("Introduce el id del registro a modificar: "))
    nombre = input("Introduce el nombre (antes era:"+agenda[identificador]['nombre']+"): ")
    email = input("Introduce el email (antes era:"+agenda[identificador]['email']+"): ")
    telefono = input("Introduce el teléfono (antes era:"+agenda[identificador]['telefono']+"): ")
    agenda[identificador] = {"nombre":nombre,"email":email,"telefono":telefono}
def eliminaRegistro():
    system('cls')
    print("Vamos a eliminar un registro")
    identificador = input("Introduce el id del registro que quieres eliminar: ")
    agenda.pop(int(identificador))
def salir():
    system('cls')
    print("Salimos del programa")
    archivo = open("agenda.txt","w")
    json.dump(agenda, archivo)
    quit()
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
