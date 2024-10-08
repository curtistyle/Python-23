from datetime import datetime

def people() -> list:
    return [
        Person("Jose", "Acuña", 23, "Concepcion del Uruguay"),
        Person("Carlos", "Alvarez", 23, "Boedo"),
        Person("Luis", "Marinez", 23, "Parana"),
        Person("Marta", "Acuña", 23, "Gualeguaychu"),
        Person("Cristian", "Rojo", 23, "Concepcion del Uruguay"),
        Person("Ana", "Aguero", 23, "Concepcion del Uruguay"),
        Person("Lautaro", "Pezella", 23, "Urdinarrain")
    ]


class Person:
    
    def __init__(self, name, lastname, age, country) -> None:
        self.name = name
        self.lastname = lastname
        self.age = age
        self.country = country
    
    def birthDate(self):
        return str(datetime.now().strftime("%d:%m:%Y")[6:])
        
    def __repr__(self) -> str:
        return f"Person({self.name}, {self.lastname}, {self.age}, {self.country})"
        
if __name__=="__main__":
    
    texto = "Welcome"
    
    print(f"{texto:_>10}")
    print(f"{texto:_<10}")
    print(f"{texto:_^10}")