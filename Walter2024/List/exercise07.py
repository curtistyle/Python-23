from random import randint


# TODO: CONCATENAR DOS LISTAS, UNA ATRAS DE LA OTRA

lista_a = list()
lista_b = list()

for number in range(10):
    lista_a.append(randint(1, 20))
    lista_b.append(randint(1, 20))
    
lista_c = list()

# ! METODO 1 
print(" > METODO 1: \n")

TAMANIO = len(lista_a) + len(lista_b)

for indice in range(0, TAMANIO):
    if indice < len(lista_a):
        lista_c.append(lista_a[indice])
    else:
        lista_c.append(lista_b[indice - TAMANIO])
        

print(
    f"{lista_a=} : {len(lista_a)}\n",
    f"{lista_b=} : {len(lista_b)}\n",
    f"{lista_c=} : {len(lista_c)}"
)

# ! METODO 2
print("\n > METODO 2: \n")

lista_c = []

while (len(lista_b) != 0):
    if len(lista_a) > 0:
        lista_c.append(lista_a.pop(0))
    else:
        lista_c.append(lista_b.pop(0))
        
print(f"{lista_c=} : {len(lista_c)}")


# ! METODO 3:
print("\n > METODO 3: \n")

for number in range(10):
    lista_a.append(randint(1, 20))
    lista_b.append(randint(1, 20))

lista_c = []

print(
    f"Before: \n"
    f"{lista_a=} : {len(lista_a)}\n",
    f"{lista_b=} : {len(lista_b)}\n",
    f"{lista_c=} : {len(lista_c)}"
)

while not (lista_b == []):
    while not (lista_a == []):
        lista_c.append(lista_a.pop(0))
    lista_c.append(lista_b.pop(0))


print(
    f"After: \n"
    f"{lista_a=} : {len(lista_a)}\n",
    f"{lista_b=} : {len(lista_b)}\n",
    f"{lista_c=} : {len(lista_c)}"
)    

# TODO: CONCATENAR DOS LISTAS EN UNA SOLA OMITIENDO LOS DATOS REPETIDOS Y MANTENIENDO SU ORDEN.

print(f"\n TODO: CONCATENAR DOS LISTAS EN UNA SOLA OMITIENDO LOS DATOS REPETIDOS Y MANTENIENDO SU ORDEN: \n")

lista_a = list()
lista_b = list()

for number in range(10):
    lista_a.append(randint(1, 20))
    lista_b.append(randint(1, 20))
    
lista_c = list()

print(
    f"Bofore: \n"
    f"{lista_a=} : {len(lista_a)}\n",
    f"{lista_b=} : {len(lista_b)}\n",
    f"{lista_c=} : {len(lista_c)}"
)   

while not lista_b == []:
    while not lista_a == []:
        if not lista_a[0] in lista_c:
            lista_c.append(lista_a.pop(0))
        else:
            lista_a.pop(0)
    if not lista_b[0] in lista_c:
        lista_c.append(lista_b.pop(0))
    else:
        lista_b.pop(0)


print(
    f"After: \n"
    f"{lista_a=} : {len(lista_a)}\n",
    f"{lista_b=} : {len(lista_b)}\n",
    f"{lista_c=} : {len(lista_c)}"
)   


#TODO: contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;

print(f"\n INTERSECCION ENTRE DOS LISTAS:")
print(f"\n METODO 1: \n")

lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_b = [3, 4, 5, 6, 7 , 8]

count = 0

for number in lista_a:
    if number in lista_b:
        count += 1
        
print(f"{count=}")
