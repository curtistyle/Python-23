from stack import Stack
from stack_methods import barrido
import random

lista_de_palabras = [
    "Argentina",
    "Peru",
    "Chile",
    "Uruguay",
    "Bolivia",
    "Brazil",
    "Paraguay",
    "Venezuela", 
    "*Ecuador*",
    "Colombia",
]

pila = Stack()
pila_aux = Stack()

for item in lista_de_palabras:
    pila.push(item)

barrido(pila)

anteultimo = pila.__len__() - 2

while(pila.__len__() >= anteultimo):
    aux = pila.pop()
    if not (pila.__len__() == anteultimo):
        pila_aux.push(aux)

barrido(pila_aux,message="(aux)")

while not(pila_aux.is_empty()):
    pila.push(pila_aux.pop())

barrido(pila)
