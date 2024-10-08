from Binary_Tree import cola
from Binary_Tree.BinaryTree_Generic import BinaryTree



tree = BinaryTree()

superheroes = [
    {"name": "Iron Man", "es_superheroe": True},
    {"name": "Capitan America", "es_superheroe": True},
    {"name": "Thor", "es_superheroe": True},
    {"name": "Black Widow", "es_superheroe": True},
    {"name": "Hulk", "es_superheroe": True},
    {"name": "Spider-Man", "es_superheroe": True},
    {"name": "Doctor Estrange", "es_superheroe": True},
    {"name": "Pantera Negra", "es_superheroe": True},
    {"name": "Capitana Marvel", "es_superheroe": True},
    {"name": "Scarlet Witch", "es_superheroe": True}
]

villanos = [
    {"name": "Thanos", "es_superheroe": False},
    {"name": "Loki", "es_superheroe": False},
    {"name": "Ultron", "es_superheroe": False},
    {"name": "Zemo", "es_superheroe": False},
    {"name": "Vulture", "es_superheroe": False},
    {"name": "Hela", "es_superheroe": False},
    {"name": "Ego", "es_superheroe": False},
    {"name": "Killmonger", "es_superheroe": False},
    {"name": "Dormammu", "es_superheroe": False},
    {"name": "Mysterio", "es_superheroe": False}
]

from random import shuffle

personajes = superheroes + villanos

shuffle(personajes)

for personaje in personajes:
    print(personaje)

# todo: a. Además del name del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente.

# * creamos el arbol
tree = BinaryTree()

for personaje in personajes:
    tree.insert_node(personaje, "name")
    
# todo: b. Listar los villanos ordenados alfabéticamente.

print(f"Listado ordenado de todos los villanos")

def by_villanos(value):
    return value["es_superheroe"] == True

lista_villanos = tree.where(by_villanos)
lista_villanos.sort(key=lambda value:value["name"])

print("\nListado ordenado de los villanos: ")
for villano in lista_villanos:
    print(" ", villano["name"])
    
# todo: c. mostrar todos los superhéroes que empiezan con C.

def by_start_c(value):
    if value["name"].startswith("C") and (value["es_superheroe"] == True):
        print(value["name"])

    
print("\nMustra todos los superheroes que empiezan con C.")

tree.select(by_start_c)
    

# todo: d. determinar cuántos superhéroes hay el árbol;

def is_hero(value):
    return value["es_superheroe"] == True

print(f"\nHay {len(tree.where(is_hero))} superheroes en el arbol")

# todo: e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;

print(f"Doctor Strange esta mal cargado. A continuacion usamos la busqueda por proximidad para encontrar y modificar el nombre.")

buscar = input("Buscar: ")

resutaldos = tree.nearby_search(buscar, "name")

if resutaldos != []:
    print(f"Se encontraron {len(resutaldos)} resultados...")
    for index, item in enumerate(resutaldos):
        print(f"[{index}] {item["name"]}")

    print("\nSeleccione el numero del nombre que desea modificar: ", end="")
    indice = int(input())

    nuevo_valor = input("Ingrese el nuevo valor: ")
    
    tree.replace(resutaldos[indice]["name"], nuevo_valor, "name")
else:
    print("Se encontraron 0 resultados.")
    
# todo: f. listar los superhéroes ordenados de manera descendente;

tree.postorden("name", by_villanos)

# ? g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a 
# ?    los villanos, luego resolver las siguiente tareas:
# ?         I. determinar cuántos nodos tiene cada árbol;
# ?         II. realizar un barrido ordenado alfabéticamente de cada árbol.

# * Generamos los dos arboles

heroes = BinaryTree()
villanos = BinaryTree()

# * Creamos el bosque

tree.forest(heroes, villanos, key_compare="es_superheroe", key_insert="name")

bosque = [heroes, villanos]

print(f"\nCantidad de nodos de los arboles Heroes: ")
print(f"N de nodos (heroes): {heroes.count_nodes()["n_nodos"]}\n")
print(f"N de nodos (villanos): {villanos.count_nodes()["n_nodos"]}")

# * Lo mostramos alfabeticamente

print(f"\nBosque. ")
print(f"\n # Heroes. ")
heroes.inorden(key="name")
print(f"\n # Villanos. ")
villanos.inorden(key="name")





