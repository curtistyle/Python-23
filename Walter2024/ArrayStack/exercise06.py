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
    

barrido(pila, message="Palabra invertida > ")
