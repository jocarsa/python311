class Persona:
    def __init__(self):
        self.nombre = ""
    def dimeNombre(self):
        return self.nombre
    def tomaNombre(self,nuevonombre):
        self.nombre = nuevonombre

Daniel = Persona()
Daniel.tomaNombre("Daniel") 
JoseVicente = Persona()
JoseVicente.tomaNombre("Jose Vicente") 

print(Daniel.dimeNombre())
print(JoseVicente.dimeNombre())

    
