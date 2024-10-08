from random import randint
from BinaryTree import BinaryTree, Node

def generateNumbersRandom(count) -> list:
    temp = []
    for index in range(0, count):
        temp.append(randint(0, 100))
    return temp

# lista auxiliar difinida
aux = [22, 12, 44, 33, 12, 54, 1, 34]

# genero la lista randomica con los numeros enteros
listOfNumbers = generateNumbersRandom(100)

# creo un arbol binario
tree_number = BinaryTree()

# inserto los elementos de la lista de numeros en el arbol
BinaryTree().list_to_tree(tree_number, aux)
# for number in listOfNumbers:
#     tree_number.insert_node(number)

# TODO: a. realizar los barridos preorden, postorden, inorden y por nivel sobre el arbol generado.

print("Barrido PRE-ORDEN: ")
tree_number.preorden()
print("\nBarrido IN-ORDEN: ")
tree_number.inorden()
print("\nBarrido PRE-ORDEN: ")
tree_number.posorden()
print()

# TODO: b. determina si un numero esta cargado en el arbol o no.
buscar = 22
print(f"\nDetermina si el numero {buscar} esta en el arbol.")
res = tree_number.search(buscar)
print(res.value if res is not None else "")

# TODO: c. eliminar tres valores del arbol
print(f"\nIngrese el valor del nodo que desea eliminar: ", end="")
eliminar = int(input())
res = tree_number.delete_node(eliminar)
print(f"\nBarrido preorden: ")
tree_number.preorden()

# TODO: d. determinar la altura del subarbol izquierdo y el subarbol derecho
# TODO: e. determinar la cantidad de ocurrencias de un elemento en el arbol

def determinar_ocurrencias(arbol : BinaryTree, valor):
    def __ocurrencias(root, valor):
        if root is not None:
            if root.value == valor:
                return 1 + __ocurrencias(root.left, valor)
            
    contador = 0
    if arbol.root is not None:
        contador = __ocurrencias(arbol.root, valor)
    return contador
