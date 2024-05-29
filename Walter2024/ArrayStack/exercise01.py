from stack import Stack
import random

pila = Stack()

# ? Carga elementos en la pila de forma randomica
print("Elementos: ", end="")
for index in range(0, 20):
    elemento = random.randint(1, 10) 
    print(f"{elemento} ", end="")
    pila.push(elemento)

comparador = int(input("\n\nIngrese elemento que desea comprar: "))

contador = 0
while not (pila.is_empty()):
    if (pila.pop() == comparador):
        contador = contador + 1

print(f"\nEl numero de ocurrencias del elemento \'{comparador}\' es: {contador}.")

