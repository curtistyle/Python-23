from random import randint
from list import barrido, quitar

def quitar_ocurrencias(lyst: list, *args):
    for element in lyst:
        if element in args:
            quitar(lyst, element)

letras = list()

for i in range(30):
    letras.append(chr(randint(97, 122)))
    
barrido(letras)

quitar_ocurrencias(letras, "a", "e", "i", "o", "u")

barrido(letras)