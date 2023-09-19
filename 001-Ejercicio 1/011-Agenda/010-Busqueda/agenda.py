# Programa agenda por Jose Vicente Carratalá Sanchis

agenda = []

def menu():
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
    opcion = input()
    print("Has seleccionado la opcion: "+opcion)
    if(opcion == "1"):
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
    elif(opcion == "2"):
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
    elif(opcion == "3"):
        print("Vamos a insertar un registro")
        nombre = input("Introduce el nombre: ")
        email = input("Introduce el email: ")
        telefono = input("Introduce el teléfono: ")
        agenda.append({"nombre":nombre,"email":email,"telefono":telefono})
    elif(opcion == "4"):
        print("Vamos a modificar un registro")
    elif(opcion == "5"):
        print("Vamos a eliminar un registro")
    elif(opcion == "6"):
        print("Salimos del programa")
    menu()

menu()
