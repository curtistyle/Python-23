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

print()

while not (pila.is_empty()):
    pila_aux.push(pila.pop())

barrido(pila_aux, message="(aux) ")

while not (pila_aux.is_empty()):
    pila.push(pila_aux.pop())
    
barrido(pila)





