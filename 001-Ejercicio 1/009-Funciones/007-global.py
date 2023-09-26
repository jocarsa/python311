edad = 45

def dimeEdad():
    print("Tu edad es de:",edad)

def cambiaEdad(nuevaedad):
    global edad
    edad = nuevaedad
    print("Tu edad es de:",edad)
    

dimeEdad()
cambiaEdad(46)
dimeEdad()
