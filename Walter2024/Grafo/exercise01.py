from grafo import Graph
from random import randint, choice
from cola import Queue

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

g = Graph()

numeros_aleatorios = [15, 32, 7, 98, 42, 6, 81, 23, 55, 10,
                     3, 76, 49, 2, 91, 85, 67, 12, 5, 88]

# * insertamos los vertices del grafo
for indice in range(len(numeros_aleatorios)):    
    g.insert_vertice(numeros_aleatorios[indice])

# * insertamos las relaciones (aristas)
for indice in range(len(numeros_aleatorios)//2):
    origen = choice(numeros_aleatorios)
    destino = choice(numeros_aleatorios)

    # * si ya existe una relacion, la omitimos
    if (g.search_arista(origen, destino) is None):
        if (origen != destino):
            g.insert_arista(origen, destino, randint(1,10))
        else:
            g.insert_arista(origen, destino, 0)
    else:
        print(f"{color.RED}Se intento insertar una misma aristsa{color.END} {origen=}, {destino=}")

print()
print()
def barrido(grafo : Graph):
    for vertice in grafo.elements:
        print(f"El valor {color.GREEN}\'{vertice['value']}\'{color.END} se relaciona con ", end="")
        if (vertice['aristas'] == []):
            print("nadie", end="")
        else:
            for indice, arista in enumerate(vertice['aristas']):
                print(f"el valor {color.GREEN}\'{arista['value']}\'{color.END}, {color.RED}P({arista['peso']}){color.END}", end=(" & " if (indice+1 != (len(vertice['aristas']))) else " "))
        print()
    

barrido(g)

relacionados = []

def no_relacionados(graph : Graph) -> list:
    temp = []
    nodos = graph.elements.copy()
    for nodo in nodos:
        if ((nodo["aristas"] != []) and (nodo["visitado"] == False)):
            nodo["visitado"] = True
            for arista in nodo['aristas']:
                temp.append(arista)
            while (len(temp) > 0):
                valor = temp[0]['value']
                temp.pop(0)
                for buscado in g.elements:
                    if(buscado['value'] == valor):
                        buscado['visitado'] = True
    temp.clear()
    for nodo in nodos:
        if (nodo['visitado'] == False):
            temp.append(nodo)
    return temp


for nodo in no_relacionados(g):
    print(f"{color.RED}Se elimino: {color.END}{nodo}")
    g.delete_vertice(nodo['value'])

print(f"\n{color.BLUE}Barrido con vertices con relacion{color.END}")
barrido(g)

def mayor_cantidad_aristas_saliente(grap: Graph):
    nodos_salientes = []
    mayor = 0
    for nodo in grap.elements:
        if len(nodo['aristas']) > mayor:
            nodos_salientes.clear()
            nodos_salientes.append(nodo)
            mayor = len(nodo['aristas'])
        elif len(nodo['aristas']) == mayor:
            nodos_salientes.append(nodo)
    return (nodos_salientes, mayor)

def mayor_cantidad_aristas_entrante(grap: Graph)->dict:
    contador={}
    vertices_entrantes=[]
    for nodo in grap.elements:
        for arista in nodo['aristas']:
            if not arista['value'] in contador.keys():
                contador.update({arista['value']:1})
            else:
                contador[arista['value']] += 1
    maximo=max(contador.values())

    for clave, valor in contador.items():
        if valor == maximo:
            vertices_entrantes.append(grap.elements[grap.search(clave)])
    return (vertices_entrantes, maximo)

print(f"\n{color.BLUE}Nodos (vertice) con mayor cantidad de aristas que entran ne el: {color.END}")
nodos=mayor_cantidad_aristas_entrante(g)
for nodo in nodos[0]:
    print(nodo)
print(f"\rCantidad de aristas que entran por vertice={nodos[1]}")

print(f"\n{color.BLUE}Nodos (vertice) con mayor cantidad de aristas que salen de el: {color.END}")
nodos=mayor_cantidad_aristas_saliente(g)
for nodo in nodos[0]:
    print(nodo)
print(f"\rCantidad de aristas que entran por vertice={nodos[1]}")

print(f"\n{color.BLUE}Cantidad de vertices del grafo: {len(g.elements)}{color.END}")

print(f"\'{color.BLUE}Aristas que apuntan a si mismo. {color.END}")

def determinar_cantidad_ciclo_directo():
    nodos = []
    for nodo in g.elements:      
        res = g.search_arista(nodo['value'], nodo['value']) 
        if res is not None:
            nodos.append(g.elements[res[0]])
    return nodos
resultado=determinar_cantidad_ciclo_directo()
print(resultado)
print(f"Cantidad={len(resultado)}")
            
# ! barrido profundidad
def aristas_mayor_peso(graph:Graph):
    resultado = { "mayor_peso" : 0, "nodos" : [] }
    
    for nodo in graph.elements:
        for adyacente in nodo['aristas']:
            peso = adyacente['peso']
            if peso == resultado['mayor_peso']:
                resultado['nodos'].append(nodo)
            if peso > resultado['mayor_peso']:
                resultado['mayor_peso'] = peso
                resultado['nodos'].clear()
                resultado['nodos'].append(nodo)
    
    return resultado
                
    

resultado=aristas_mayor_peso(g)

print(f"{color.BLUE}Aristas con el camino mas largo, (mayor peso){color.END}")

for arista in resultado['nodos']:
    print(f"Origen \'{color.GREEN}{arista['value']}{color.END}\' -> Destino ", end="") 
    for adyacente in arista['aristas']:
        if adyacente['peso'] == resultado['mayor_peso']:
            print(f"\'{color.RED}{adyacente['value']}{color.END}\' | Peso : {color.PURPLE}{resultado['mayor_peso']}{color.END}")