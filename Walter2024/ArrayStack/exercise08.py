from stack import Stack
from stack_methods import barrido
from random import sample, shuffle
from dataclasses import dataclass

mazo_de_cartas = Stack()

@dataclass
class Carta:
    palo: str
    numero: int

    def __str__(self) -> str:
        return f"Palo: {self.palo}, Numero: {self.numero}"

    def __repr__(self) -> str:
        return f"Carta({self.palo=}, {self.numero=})"
    


 
if __name__=="__main__":

    palos = ["Basto", "Espada", "Oro", "Copa"]
    
    lista_cartas = []
    for palo in palos:
        for numero in range(1, 13):
            lista_cartas.append(Carta(palo, numero))
            
    shuffle(lista_cartas)       
    
    for carta in lista_cartas:
        mazo_de_cartas.push(carta)
    
    print("Mazo desordenado.", end="\n")
    barrido(mazo_de_cartas,"","\n")
    
    pila_basto = Stack()
    pila_espada = Stack()
    pila_oro = Stack()
    pila_copa = Stack()
    
    while not(mazo_de_cartas.is_empty()):
        if (mazo_de_cartas.top().palo == "Basto"):
            carta = mazo_de_cartas.pop()
            pila_basto.push(carta)
        elif (mazo_de_cartas.top().palo == "Espada"):
            carta = mazo_de_cartas.pop()
            pila_espada.push(carta)
        elif (mazo_de_cartas.top().palo == "Oro"):
            carta = mazo_de_cartas.pop()
            pila_oro.push(carta)
        else:
            carta = mazo_de_cartas.pop()
            pila_copa.push(carta)
            
    
    barrido(pila_basto, "Basto=>", "\n")
    barrido(pila_copa, "Copa=>", "\n")
    barrido(pila_oro, "Oro=>", "\n")
    barrido(pila_espada, "Espada=>", "\n")
    
    