from dataclasses import dataclass


def validar_entrada(funcion):
    def wrapper(*args, **kwargs):
        for arg in args:
            if (len(arg) > 30):
                raise TabError("Los parametros de entrada no pueden superar los 30 caracteres.")
        return funcion(arg, **kwargs)
    return wrapper
        

@dataclass
class Persona:
    name: str 
    lastName: str 
    
    @validar_entrada
    def setName(self, value):
        self.name = value
    
    def __len__(self):
        return len(self.name)
    

estudiante = Persona("Marta", "Perez")

estudiante.setName("Carlos")

print(estudiante)

