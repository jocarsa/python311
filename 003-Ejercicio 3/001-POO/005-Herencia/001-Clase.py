class Ser:
    def __init__(self):
        self.posx = 0
        self.posy = 0

class Persona(Ser):
    def __init__(self):
        super().__init__()
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
print(Daniel.posx)

    
