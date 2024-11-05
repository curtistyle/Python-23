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

class Maravilla:
    def __init__(self, nombre, ubicacion, tipo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tipo = tipo

    def __eq__(self, value) -> bool:
        if isinstance(value, Maravilla):
            return self.nombre == value.nombre
        return False

    def __ne__(self, value) -> bool:
        return self.nombre != value.nombre

    def __lt__(self, value) -> bool:
        return self.nombre < value.nombre

    def __le__(self, value) -> bool:
        return self.nombre <= value.nombre

    def __gt__(self, value) -> bool:
        return self.nombre > value.nombre

    def __ge__(self, value) -> bool:
        return self.nombre >= value.nombre

    def __iter__(self):
        return iter(self.nombre)

    # def __hash__(self):
    #     return hash(self.nombre)
    
    def __repr__(self):
        # f"La maravilla {self.nombre} ubicada en {self.ubicacion} y del tipo {self.tipo}"
        return f"{self.nombre}"

    def __str__(self) -> str:
        return f"{self.nombre}"
    # def __str__(self):
    #     return f"{self.__class__.__name__}(nombre={self.nombre!r},ubicacion={self.ubicacion!r},tipo={self.tipo!r})"


class Maravillas:
    CHICHEN_ITZA = Maravilla("Chichén Itzá", "Mexico", "Arquitectonica")
    COLISEO_DE_ROMA = Maravilla("Coliseo de Roma", "Italia", "Arquitectonica")
    ESTATUA_CRISTO_REDENTOR = Maravilla("Estatua del Cristo Redentor", "Brazil", "Arquitectonica")
    MURALLA_CHINA = Maravilla("Gran Muralla China", "China", "Arquitectonica")
    MACHU_PICCHU = Maravilla("Machu Picchu", "Peru", "Arquitectonica")
    PETRA = Maravilla("Petra", "Jordania", "Arquitectonica")
    TAJ_MAHAL = Maravilla("Taj Mahal", "India", "Arquitectonica")
    CATARATAS_IGUAZU = Maravilla("Cataratas del Iguazu", "Argentina/Brazil", "Natural")
    CANON_DEL_COLORADO = Maravilla("Gran Cañon del Colorado", "Estados Unidos", "Natural")
    MOAIS = Maravilla("Moáis de la Isla de Pascua", "Chile", "Natural")






grafo_maravillas = Graph(dirigido=False)

# insercion de los vertives

grafo_maravillas.insert_vertice(Maravillas.CHICHEN_ITZA)
grafo_maravillas.insert_vertice(Maravillas.COLISEO_DE_ROMA)
grafo_maravillas.insert_vertice(Maravillas.ESTATUA_CRISTO_REDENTOR)
grafo_maravillas.insert_vertice(Maravillas.MURALLA_CHINA)
grafo_maravillas.insert_vertice(Maravillas.MACHU_PICCHU)
grafo_maravillas.insert_vertice(Maravillas.CATARATAS_IGUAZU)
grafo_maravillas.insert_vertice(Maravillas.PETRA)

# insercion de las aristas

grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.COLISEO_DE_ROMA,randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.ESTATUA_CRISTO_REDENTOR, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.MURALLA_CHINA, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.MACHU_PICCHU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.CATARATAS_IGUAZU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.CHICHEN_ITZA, Maravillas.PETRA, randint(100, 10000))

grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA, Maravillas.ESTATUA_CRISTO_REDENTOR, randint(100,10000))
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA, Maravillas.MURALLA_CHINA, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA, Maravillas.MACHU_PICCHU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA, Maravillas.CATARATAS_IGUAZU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.COLISEO_DE_ROMA, Maravillas.PETRA, randint(100, 10000))

grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR, Maravillas.MURALLA_CHINA, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR, Maravillas.MACHU_PICCHU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR, Maravillas.CATARATAS_IGUAZU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.ESTATUA_CRISTO_REDENTOR, Maravillas.PETRA, randint(100, 10000))

grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA, Maravillas.MACHU_PICCHU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA, Maravillas.CATARATAS_IGUAZU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.MURALLA_CHINA, Maravillas.PETRA, randint(100, 10000))

grafo_maravillas.insert_arista(Maravillas.MACHU_PICCHU, Maravillas.CATARATAS_IGUAZU, randint(100, 10000))
grafo_maravillas.insert_arista(Maravillas.MACHU_PICCHU, Maravillas.PETRA, randint(100, 10000))

grafo_maravillas.insert_arista(Maravillas.CATARATAS_IGUAZU, Maravillas.PETRA, randint(100, 10000))


for vertice in grafo_maravillas.elements:
    print(f"La Maravilla {color.GREEN}{vertice["value"].nombre!r}{color.END} se relaciona con")
    for adyacente in vertice["aristas"]:
        print(f" -> {color.CYAN}{adyacente["value"].nombre!r}{color.END} a una distancia de {color.RED}{adyacente["peso"]}{color.END} km.")


bosque = []


print(Maravillas.CHICHEN_ITZA == grafo_maravillas.elements[0]["value"])
input()

arbol = grafo_maravillas.kruskal(Maravillas.COLISEO_DE_ROMA)

#print(arbol)

#for vertice in grafo_maravillas.elements:
#    bosque.append({"valor" : vertice["value"], "arbol_expansion_minima" : grafo_maravillas.kruskal(vertice["value"])})


