from stack import Stack
import random

pila = Stack()
pila_aux = Stack()

# ? Carga elementos en la pila de forma randomica
print("Elementos: ", end="")
for index in range(0, 20):
    elemento = random.randint(1, 10) 
    print(f"{elemento} ", end="")
    pila.push(elemento)
    
input("\n\nQuitar impares:")
    
while not (pila.is_empty()):
    if ((pila.top() % 2) != 0):
        print(pila.pop(), end="")
    else:
        pila_aux.push(pila.pop())

print(f"\n\n Stack sin elementos impares: ")
# ! barrido
while not (pila_aux.is_empty()):
    aux = pila_aux.pop()
    print(f"{aux} ", end="")
    pila.push(aux)
    
