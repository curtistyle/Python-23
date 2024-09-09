from Binary_Tree import cola
from Binary_Tree.BinaryTree_Generic import BinaryTree

# todo: a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;

tree = BinaryTree()

superheroes = [
    {"nombre": "Iron Man", "es_superheroe": True},
    {"nombre": "Capitán América", "es_superheroe": True},
    {"nombre": "Thor", "es_superheroe": True},
    {"nombre": "Black Widow", "es_superheroe": True},
    {"nombre": "Hulk", "es_superheroe": True},
    {"nombre": "Spider-Man", "es_superheroe": True},
    {"nombre": "Doctor Strange", "es_superheroe": True},
    {"nombre": "Pantera Negra", "es_superheroe": True},
    {"nombre": "Capitana Marvel", "es_superheroe": True},
    {"nombre": "Scarlet Witch", "es_superheroe": True}
]

villanos = [
    {"nombre": "Thanos", "es_superheroe": False},
    {"nombre": "Loki", "es_superheroe": False},
    {"nombre": "Ultrón", "es_superheroe": False},
    {"nombre": "Zemo", "es_superheroe": False},
    {"nombre": "Vulture", "es_superheroe": False},
    {"nombre": "Hela", "es_superheroe": False},
    {"nombre": "Ego", "es_superheroe": False},
    {"nombre": "Killmonger", "es_superheroe": False},
    {"nombre": "Dormammu", "es_superheroe": False},
    {"nombre": "Mysterio", "es_superheroe": False}
]

from random import shuffle

personajes = superheroes + villanos

shuffle(personajes)

for personaje in personajes:
    print(personaje)

