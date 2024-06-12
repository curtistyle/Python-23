from list import barrido
from random import randint

lista_numeros = list()

for numero in range(20):
    lista_numeros.append(randint(1, 100))
    
barrido(lista_numeros)

lista_par = list()
lista_impar = list()

for indice, numero in enumerate(lista_numeros):
    if ((numero % 2) == 0):
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
        

print(f"Lista numeros pares: ")
barrido(lista_par)

print(f"Lista numeros impares: ")
barrido(lista_impar)



