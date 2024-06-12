from list import barrido, quitar
from random import randint


def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


lista_numeros = list()

for index in range(30):
    lista_numeros.append(randint(1,100))
    
barrido(lista_numeros)

for element in lista_numeros:
    if es_primo(element):
        print(f"Se quito: {element}.")
        quitar(lista_numeros, element)

barrido(lista_numeros)
