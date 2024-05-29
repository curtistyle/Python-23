from stack import Stack
from stack_methods import barrido
import random

pila = Stack()
pila_invertida = Stack()
pila_aux = Stack()

palabra = input("Ingrese una palabra: ")

for item in palabra:
    print(item)
    pila.push(item)
    

while not (pila.is_empty()):
    aux = pila.pop()
    pila_aux.push(aux)
    pila_invertida.push(aux)

while not(pila_aux.is_empty()):
    pila.push(pila_aux.pop())
    
barrido(pila)

while not(pila.is_empty()):
    if (pila.top() == pila_invertida.top()):
        pila_invertida.pop()
    pila.pop()

if (pila_invertida.is_empty()):
    print(f"\'{palabra}\' es palindromo.")    
else:
    print(f"\'{palabra}\' NO es palindromo.")

