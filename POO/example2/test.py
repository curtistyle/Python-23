class Auto():
    
    
    ruedas = 4
    
    
    def __init__(self, color, marca, modelo) -> None:
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def __str__(self) -> str:
        return f"{self.color!r}, {self.marca!r}, {self.modelo!r}"
    
    def __repr__(self) -> str:
        return f"{self.color!r}, {self.marca!r}, {self.modelo!r}, {self.ruedas!r}"

    @classmethod
    def cantidadRuedas(cls, value):
        c = cls
        c.ruedas = value
        


auto1 = Auto("Rojo", "Toyota", 2010)
auto2 = Auto("Verde", "Volkswagen", 2020)
auto3 = Auto("Negro", "Ford", 2023)

print("A: ")
print(f"{auto1=} \n{auto2=} \n{auto3=}")

Auto.cantidadRuedas(3)


print("\nB: ")
auto4 = Auto("Azul", "Mercedes Benz", 2000)
print(f"{auto1=} \n{auto2=} \n{auto3=} \n{auto4=}")
    