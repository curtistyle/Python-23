from stack import Stack
from stack_methods import barrido
import random

pila = Stack()
pila_aux = Stack()

# ? Carga elementos en la pila de forma randomica
print("Elementos: ", end="")
for index in range(0, 20):
    elemento = random.randint(1, 10) 
    print(f"{elemento} ", end="")
    pila.push(elemento)
    
ocurrencia = int(input("\n\nIngrese la ocurrencia que desea reemplazar: "))
nuevo_valor = int(input("\nIngrese el nuevo valor: "))

while not (pila.is_empty()):
    if (pila.top() == ocurrencia):

        pila_aux.push(nuevo_valor)
        pila.pop()
    else:
        pila_aux.push(pila.pop())

barrido(pila_aux)