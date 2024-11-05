""" 14. Implementar sobre un grafo_ambientes no dirigido los algoritmos necesario para dar solución a las si-
        guientes tareas:
    a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
        baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
    b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
        ta es la distancia entre los ambientes, se debe cargar en metros;
    c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
        para conectar todos los ambientes;
    d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
        determinar cuántos metros de cable de red se necesitan para conectar el router con el
        Smart Tv. """
from gc import collect

from grafo import Graph
from random import randint

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


ambientes = [
    "Cocina",
    "Comedor",
    "Cochera",
    "Quincho",
    "Baño 1",
    "Baño 2",
    "Habitacion 1",
    "Habitacion 2",
    "Sala de Estar",
    "Terraza",
    "Patio"
]


grafo_ambientes = Graph(dirigido=False)

temp_ambientes = ambientes.copy()

for ambiente in ambientes:
    grafo_ambientes.insert_vertice(ambiente)


# * insercion de aristas


grafo_ambientes.insert_arista("Sala de Estar", "Baño 1", 3)
# grafo_ambientes.insert_arista("Sala de Estar", "Comedor", 1)
# grafo_ambientes.insert_arista("Sala de Estar", "Cochera", 4)

# grafo_ambientes.insert_arista("Cochera", "Patio", 1)
# grafo_ambientes.insert_arista("Cochera", "Comedor", 2)
grafo_ambientes.insert_arista("Cochera", "Sala de Estar", 4)
grafo_ambientes.insert_arista("Cochera", "Quincho", 3)
# grafo_ambientes.insert_arista("Cochera", "Cocina", 5)

grafo_ambientes.insert_arista("Comedor", "Sala de Estar", 1)
grafo_ambientes.insert_arista("Comedor", "Cochera", 2)
# grafo_ambientes.insert_arista("Comedor", "Cocina", 1)
grafo_ambientes.insert_arista("Comedor", "Terraza", 10)
grafo_ambientes.insert_arista("Comedor", "Habitacion 2", 5)
grafo_ambientes.insert_arista("Comedor", "Habitacion 1", 2)
grafo_ambientes.insert_arista("Comedor", "Baño 1", 3)

grafo_ambientes.insert_arista("Patio", "Cochera", 1)
# grafo_ambientes.insert_arista("Patio", "Quincho", 1)
# grafo_ambientes.insert_arista("Patio", "Cocina", 3)

# grafo_ambientes.insert_arista("Quincho", "Cocina", 5)
grafo_ambientes.insert_arista("Quincho", "Patio", 1)
#grafo_ambientes.insert_arista("Quincho", "Cochera", 3)

grafo_ambientes.insert_arista("Cocina", "Quincho", 5)
grafo_ambientes.insert_arista("Cocina", "Patio", 3)
grafo_ambientes.insert_arista("Cocina", "Cochera", 5)
grafo_ambientes.insert_arista("Cocina", "Comedor", 1)

# grafo_ambientes.insert_arista("Baño 1", "Sala de Estar", 3)
# grafo_ambientes.insert_arista("Baño 1", "Comedor", 3)
grafo_ambientes.insert_arista("Baño 1", "Habitacion 2", 7)
grafo_ambientes.insert_arista("Baño 1", "Habitacion 1", 1)

# grafo_ambientes.insert_arista("Habitacion 1", "Baño 1", 1)
# grafo_ambientes.insert_arista("Habitacion 1", "Comedor", 2)
# grafo_ambientes.insert_arista("Habitacion 1", "Habitacion 2", 5)
grafo_ambientes.insert_arista("Habitacion 1", "Baño 2", 10)

# grafo_ambientes.insert_arista("Habitacion 2", "Comedor", 5)
# grafo_ambientes.insert_arista("Habitacion 2", "Baño 1", 7)
grafo_ambientes.insert_arista("Habitacion 2", "Habitacion 1", 5)
# grafo_ambientes.insert_arista("Habitacion 2", "Baño 2", 1)
# grafo_ambientes.insert_arista("Habitacion 2", "Terraza", 2)

grafo_ambientes.insert_arista("Baño 2", "Terraza", 4)
grafo_ambientes.insert_arista("Baño 2", "Habitacion 2", 1)
# grafo_ambientes.insert_arista("Baño 2", "Habitacion 1", 10)

# grafo_ambientes.insert_arista("Terraza", "Baño 2", 4)
grafo_ambientes.insert_arista("Terraza", "Habitacion 2", 2)
# grafo_ambientes.insert_arista("Terraza", "Comedor", 10)


for vertice in grafo_ambientes.elements:
    print(f"El ambiente \'{color.GREEN}{vertice['value']}{color.END}\' se relaciona con ")
    for adyacente in vertice['aristas']:
        print(f" -> {color.PURPLE}\'{adyacente['value']}\'{color.END} a una distancia de {color.RED}\'{adyacente['peso']}\'{color.END} mts.")
        
# kruskal devuelve el arbol de expansion minima de un grafo_ambientes a partir de un origen
# El "arbol de expansion minima" es un subgrafo_ambientes que conecta todos los vertices del grafo_ambientes original de la manera mas eficiente posible, es decir,
# con el peso total minimo de sus aristas.
arbol_expansion = grafo_ambientes.kruskal("Cocina")



print("\n")

print(f"|{color.GREEN}{"origen":^15}{color.END}|{color.RED}{"Destino":^15}{color.END}|{color.CYAN}{"Peso":^8}{color.END}|")
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"| {origen:<14}| {destino:<14}| {peso:>6} |")

def calcular_metros_cable(arbol):
    acumador = 0
    for arista in arbol[0].split(';'):
        origen, destino, peso = arista.split('-')
        acumador = acumador + int(peso)
    return acumador

print(f"\n{color.BLUE}Se necesitan{color.END} {color.GREEN}{calcular_metros_cable(arbol_expansion)} mts{color.END} {color.BLUE}de cable para conectar todos los ambientes.{color.END}")

def determinar_camino_mas_corto(grafo_ambientes, origen, destino):
    """determina el camino mas corto utilizando el algotirmo de dijkstra"""
    caminos = grafo_ambientes.dijkstra(origen)  # todos los caminos mas cortos desde origen hasta todos los vertices del grafo_ambientes

    peso_total = None
    camino_completo = []

    while (caminos.size() > 0):
        camino = caminos.pop()

        # camino[1][0] son todos los destinos (vertices) con menor peso, partiendo desde origen

        if (camino[1][0] == destino):
            if peso_total is None:
                peso_total = camino[0]
            camino_completo.append(camino[1][0])
            destino = camino[1][2]

    camino_completo.reverse()

    return camino_completo, peso_total

camino, peso = determinar_camino_mas_corto(grafo_ambientes, "Sala de Estar", "Habitacion 1")

print(f'\n{color.BLUE}El camino mas corto es: {color.GREEN}{f'{color.RED} -> {color.END}{color.GREEN}'.join(camino)}{color.END}{color.BLUE}, se necesitan {peso} mts de cable para la instalacion del Smart TV.{color.END}')

