from grafo import Graph
from random import randint
from cola import Queue
from heap import HeapMin
from pila import Stack



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

class Maravilla:
    def __init__(graph, nombre, ubicacion, tipo):
        graph.nombre = nombre
        graph.ubicacion = ubicacion
        graph.tipo = tipo



    # def __eq__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre == other.nombre
    #     elif isinstance(other, str):
    #         return graph.nombre == other
    #     return False
    #
    #
    # def __ne__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre != other.nombre
    #     return False
    #
    # def __lt__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre < other.nombre
    #     return False
    #
    # def __le__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre <= other.nombre
    #     return False
    #
    # def __gt__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre > other.nombre
    #     return False
    #
    # def __ge__(graph, other) -> bool:
    #     if isinstance(other, Maravilla):
    #         return graph.nombre >= other.nombre
    #     return False
    #
    #
    #
    # def __iter__(graph):
    #     graph._indice = 0  # Reiniciar el índice al comienzo
    #     return graph
    #
    # def __next__(graph):
    #     if graph._indice < len(graph.nombre):
    #         caracter = graph.nombre[graph._indice]
    #         graph._indice += 1
    #         return caracter
    #     else:
    #         raise StopIteration
    #
    # def __add__(graph, other):
    #     return graph.nombre + other.nombre
    #
    # #def __iter__(graph):
    # #    return iter(graph.nombre)
    #
    # #def __hash__(graph):
    # #    return hash(graph.nombre)
    #
    # def __repr__(graph):
    #     # f"La maravilla {graph.nombre} ubicada en {graph.ubicacion} y del tipo {graph.tipo}"
    #     return str(graph.nombre)
    #
    # def __str__(graph) -> str:
    #     return str(graph.nombre)


class Maravillas:
    CHICHEN_ITZA = Maravilla("Chichén Itzá", "Mexico", "Arquitectonica")
    COLISEO_DE_ROMA = Maravilla("Coliseo de Roma", "Italia", "Arquitectonica")
    ESTATUA_CRISTO_REDENTOR = Maravilla("Estatua del Cristo Redentor", "Brazil", "Natural") # Arquitectonica -> Natural
    MURALLA_CHINA = Maravilla("Gran Muralla China", "China", "Arquitectonica")
    MACHU_PICCHU = Maravilla("Machu Picchu", "Mexico", "Natural") # Peru -> Mexico, Arquitectonica -> Natural
    PETRA = Maravilla("Petra", "Jordania", "Natural") # Arquitectonica -> Natural
    # TAJ_MAHAL = Maravilla("Taj Mahal", "India", "Arquitectonica")
    CATARATAS_IGUAZU = Maravilla("Cataratas del Iguazu", "Argentina/Brazil", "Natural")
    # CANON_DEL_COLORADO = Maravilla("Gran Cañon del Colorado", "Estados Unidos", "Natural")
    # MOAIS = Maravilla("Moáis de la Isla de Pascua", "Chile", "Natural")

    @staticmethod
    def get_list(cls):
        return [
            Maravillas.CHICHEN_ITZA,
            Maravillas.COLISEO_DE_ROMA,
            Maravillas.ESTATUA_CRISTO_REDENTOR,
            Maravillas.MURALLA_CHINA,
            Maravillas.MACHU_PICCHU,
            Maravillas.CATARATAS_IGUAZU,
            Maravillas.PETRA
        ]


#print(Maravillas.CHICHEN_ITZA.nombre , Maravillas.MURALLA_CHINA.nombre)
#input()

grafo_maravillas = Graph(dirigido=False)

# insercion de los vertives

grafo_maravillas.insert_vertice(Maravillas.CHICHEN_ITZA.nombre, Maravillas.CHICHEN_ITZA)
grafo_maravillas.insert_vertice(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.COLISEO_DE_ROMA)
grafo_maravillas.insert_vertice(Maravillas.ESTATUA_CRISTO_REDENTOR.nombre, Maravillas.ESTATUA_CRISTO_REDENTOR)
grafo_maravillas.insert_vertice(Maravillas.MURALLA_CHINA.nombre, Maravillas.MURALLA_CHINA)
grafo_maravillas.insert_vertice(Maravillas.MACHU_PICCHU.nombre, Maravillas.MACHU_PICCHU)
grafo_maravillas.insert_vertice(Maravillas.CATARATAS_IGUAZU.nombre, Maravillas.CATARATAS_IGUAZU)
grafo_maravillas.insert_vertice(Maravillas.PETRA.nombre, Maravillas.PETRA)

# insercion de las aristas

grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.COLISEO_DE_ROMA.nombre,             10000)
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.ESTATUA_CRISTO_REDENTOR.nombre,     9500)
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.MURALLA_CHINA.nombre,               9000)
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.MACHU_PICCHU.nombre,                8500)
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.CATARATAS_IGUAZU.nombre,            8000)
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA.nombre, Maravillas.PETRA.nombre,                       7500)

grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.ESTATUA_CRISTO_REDENTOR.nombre,  7000)
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.MURALLA_CHINA.nombre,            6500)
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.MACHU_PICCHU.nombre,             6000)
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.CATARATAS_IGUAZU.nombre,         5500)
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA.nombre, Maravillas.PETRA.nombre,                    5000)

grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR.nombre, Maravillas.MURALLA_CHINA.nombre,    4500)
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR.nombre, Maravillas.MACHU_PICCHU.nombre,     4000)
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR.nombre, Maravillas.CATARATAS_IGUAZU.nombre, 3500)
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR.nombre, Maravillas.PETRA.nombre,            3000)

grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA.nombre, Maravillas.MACHU_PICCHU.nombre,               2500)
grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA.nombre, Maravillas.CATARATAS_IGUAZU.nombre,           2000)
grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA.nombre, Maravillas.PETRA.nombre,                      1500)

grafo_maravillas.insert_arista(Maravillas.MACHU_PICCHU.nombre, Maravillas.CATARATAS_IGUAZU.nombre,            1000)
grafo_maravillas.insert_arista(Maravillas.MACHU_PICCHU.nombre, Maravillas.PETRA.nombre,                       500)

grafo_maravillas.insert_arista(Maravillas.CATARATAS_IGUAZU.nombre, Maravillas.PETRA.nombre,                   10)


for vertice in grafo_maravillas.elements:
    print(f"La Maravilla {color.GREEN}{vertice["value"]!r}{color.END} se relaciona con")
    for adyacente in vertice["aristas"]:
        print(f" -> {color.CYAN}{adyacente["value"]!r}{color.END} a una distancia de {color.RED}{adyacente["peso"]}{color.END} km.")


def kruskal(graph, origen, tipo):
    def buscar_en_bosque(bosque, buscado):
        for index, arbol in enumerate(bosque):
            #print(f"{buscado=}, {arbol=}")
            #input()
            if buscado in arbol:
                return index

    bosque = []
    aristas = HeapMin()
    for nodo in graph.elements:
        bosque.append(nodo['value'])
        adjacentes = nodo['aristas']
        if (nodo['other_value'].tipo == tipo):
            for adjacente in adjacentes:

                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

    # print(aristas.elements)
    while len(bosque) > 1 and len(aristas.elements) > 0:
        arista = aristas.atention()
        # print(bosque)
        # print(arista[1][0], arista[1][1])
        # print(arista)
        origen = buscar_en_bosque(bosque, arista[1][0])
        destino = buscar_en_bosque(bosque, arista[1][1])
        # print(origen, destino)
        if origen is not None and destino is not None:
            if origen != destino:
                if origen > destino:
                    vertice_ori = bosque.pop(origen)
                    vertice_des = bosque.pop(destino)
                else:
                    vertice_des = bosque.pop(destino)
                    vertice_ori = bosque.pop(origen)

                if '-' not in vertice_ori and '-' not in vertice_des:
                    #print(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    #input("A")
                    bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                elif '-' not in vertice_des:
                    #print(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    #input("B")
                    bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                elif '-' not in vertice_ori:
                    #print(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    #input("C")
                    bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                else:
                    #print(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
                    #input("D")
                    bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
    return bosque

arbol = kruskal(grafo_maravillas, Maravillas.CATARATAS_IGUAZU.nombre, "Natural")

print(f"\nArbol de expansion minima, origen: {Maravillas.CATARATAS_IGUAZU.nombre!r}, tipo: {Maravillas.CATARATAS_IGUAZU.tipo!r}")

print(f"|{color.GREEN}{"origen":^30}{color.END}|{color.RED}{"Destino":^30}{color.END}|{color.CYAN}{"Peso":^8}{color.END}|")
for arista in arbol[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"| {origen:<29}| {destino:<29}| {peso:>6} |")

arbol = kruskal(grafo_maravillas, Maravillas.CATARATAS_IGUAZU.nombre, "Arquitectonica")

print(f"\nArbol de expansion minima, origen: {Maravillas.CHICHEN_ITZA.nombre!r}, tipo: {Maravillas.CHICHEN_ITZA.tipo!r}")

print(f"|{color.GREEN}{"origen":^30}{color.END}|{color.RED}{"Destino":^30}{color.END}|{color.CYAN}{"Peso":^8}{color.END}|")
for arista in arbol[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"| {origen:<29}| {destino:<29}| {peso:>6} |")


def maravillas_x_pais(graph, origin):
    resultado = {}
    def __deep_show(graph, origin):
        pos_vertice = graph.search(origin)
        if pos_vertice is not None:
            if not graph.elements[pos_vertice]['visitado']:
                graph.elements[pos_vertice]['visitado'] = True
                for ubicacion in graph.elements[pos_vertice]['other_value'].ubicacion.split("/"):
                    if not ubicacion in resultado.keys():
                        resultado[ubicacion] = 1
                    else:
                        resultado[ubicacion] += 1

                adyacentes = graph.elements[pos_vertice]['aristas']
                for adyacente in adyacentes:
                    __deep_show(graph, adyacente['value'])

    graph.mark_as_not_visited()
    __deep_show(graph, origin)
    return resultado

# resultado = maravillas_x_pais(grafo_maravillas, Maravillas.CHICHEN_ITZA.nombre)
# print()
# for pais, cantidad in resultado.items():
#     if (cantidad > 1):
#         print(f"El Pais {pais} tiene mas de una Maravilla, cantidad: {cantidad}")

paises = {}

for vertice in grafo_maravillas.elements:
    ubicaciones = vertice['other_value'].ubicacion.split("/")
    for ubicacion in ubicaciones:
        if not ubicacion in paises.keys():
            paises[ubicacion] = {vertice['other_value'].tipo : 1}
        else:
            if vertice['other_value'].tipo in paises[ubicacion].keys():
                paises[ubicacion][vertice['other_value'].tipo] += 1
            else:
                paises[ubicacion][vertice['other_value'].tipo] = 1

print()

for pais, tipo in paises.items():
    for clave in tipo.keys():
        if tipo[clave] > 1:
            print(f"El pais {pais!r} dispone mas de una maravilla del mismo tipo. Cantidad: {tipo[clave]}")

print()
for pais, tipo in paises.items():
    if len(tipo.keys()) > 1:
        print(f"El pais {pais!r} dispone de maravillas naturales y arquitectonica")