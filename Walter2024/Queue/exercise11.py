"""Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta 
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:"""

from cola import Queue

class Personaje:
    def __init__(self, nombre, origen) -> None:
        self.nombre = nombre
        self.origen = origen
    
    def __str__(self) -> str:
        return f"{__class__.__name__}({self.nombre=}, {self.origen=})"
    
    def __repr__(self) -> str:
        return f"\'{self.nombre}\' proviene del planeta \'{self.origen}\'."

personajes_star_wars = [
    Personaje("Luke Skywalker", "Tatooine"),
    Personaje("Leia Organa", "Alderaan"),
    Personaje("Darth Vader", "Tatooine"),
    Personaje("Han Solo", "Corellia"),
    Personaje("Yoda", "Desconocido"),
    Personaje("Obi-Wan Kenobi", "Stewjon"),
    Personaje("Jar Jar Binks", "Naboo"),
    Personaje("Padmé Amidala", "Naboo"),
    Personaje("Rey", "Jakku"),
    Personaje("Palpatine", "Naboo"),
    Personaje("Chewbacca", "Kashyyyk")
]


cola_personajes = Queue()

# * mostrar elementos de una cola

def barrido(cola : Queue):
    for indice in range(cola.size()):
        print(cola.on_front())
        cola.move_to_end()
        
# * Cargamos la cola

for personaje in personajes_star_wars:
    cola_personajes.arrive(personaje)
    
# todo: a. mostrar los personajes del planeta Alderaan, Endor y Tatooine

print("(a) Personajes del planeta Alderaan, Endor y Tatooine. \n")

for indice in range(cola_personajes.size()):
    personaje : Personaje = cola_personajes.on_front()
    cola_personajes.move_to_end()
    
    if personaje.origen in ["Alderaan", "Endor", "Tatooine"]:
        print(repr(personaje))
        
# todo: b indicar el plantea natal de Luke Skywalker y Han Solo

print("\n(b) Planeta natal del Lukle Skywalker y Han Solo. \n")

for indice in range(cola_personajes.size()):
    personaje : Personaje = cola_personajes.on_front()
    
    if personaje.nombre == "Luke Skywalker" or personaje.nombre == "Han Solo":
        print(repr(personaje))
    
    cola_personajes.move_to_end()
        
# todo: c. insertar un nuevo personaje antes del maestro Yoda

print("\n(c) Insertar un nuevo personaje antes del maestro Yoda. \n")

for indice in range(cola_personajes.size()):
    personaje : Personaje = cola_personajes.on_front()
    
    if personaje.nombre == "Yoda":
        print("Nuevo Peronaje.")
        nuevo_personaje = Personaje(
            input("Nombre: "),
            input("Planeta Origen: ")
        )
        cola_personajes.arrive(nuevo_personaje)
        
    cola_personajes.move_to_end()

print()    
barrido(cola_personajes)

# todo: d. eliminar el personaje ubicado después de Jar Jar Binks

print("\n(d) Eliminar el personaje ubicado despues de Jar Jar Binks. \n")

buscar = "Jar Jar Binks"

for indice in range(cola_personajes.size()):
    personaje : Personaje = cola_personajes.on_front()
    
    if (personaje.nombre == buscar):
        if (indice < cola_personajes.size() -1):
            cola_personajes.move_to_end()
            print(f"Se elimino a {repr(cola_personajes.on_front())}\n")
            cola_personajes.attention()      
        else:
            print("No hay nadie al final de la cola\n")
        
    cola_personajes.move_to_end()

barrido(cola_personajes)