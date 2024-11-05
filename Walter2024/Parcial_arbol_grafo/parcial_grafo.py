from grafo import Graph, Queue
from random import randint

personajes = [
    "Luke Skywalker",
    "Darth Vader",
    "Yoda",
    "Boba Fett",
    "C.3PO",
    "Leia",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2.D2",
    "BB.8"
]

# creo la instancia de un grafo no dirigido
grafo = Graph(dirigido=False)

# inserto los vertices

for personaje in personajes:
    grafo.insert_vertice(personaje)

# inserto las aristas



grafo.insert_arista("Luke Skywalker", "Darth Vader", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Yoda", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Boba Fett", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "C.3PO", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Leiar", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Rey", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Chewbacca", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "Han Solo", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "R2.D2", randint(1, 20))
grafo.insert_arista("Luke Skywalker", "BB.8", randint(1, 20))

grafo.insert_arista("Darth Vader", "Yoda", randint(1, 20))
grafo.insert_arista("Darth Vader", "Boba Fett", randint(1, 20))
grafo.insert_arista("Darth Vader", "C.3PO", randint(1, 20))
grafo.insert_arista("Darth Vader", "Leiar", randint(1, 20))
grafo.insert_arista("Darth Vader", "Rey", randint(1, 20))
grafo.insert_arista("Darth Vader", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Darth Vader", "Chewbacca", randint(1, 20))
grafo.insert_arista("Darth Vader", "Han Solo", randint(1, 20))
grafo.insert_arista("Darth Vader", "R2.D2", randint(1, 20))
grafo.insert_arista("Darth Vader", "BB.8", randint(1, 20))

grafo.insert_arista("Yoda", "Boba Fett", randint(1, 20))
grafo.insert_arista("Yoda", "C.3PO", randint(1, 20))
grafo.insert_arista("Yoda", "Leiar", randint(1, 20))
grafo.insert_arista("Yoda", "Rey", randint(1, 20))
grafo.insert_arista("Yoda", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Yoda", "Chewbacca", randint(1, 20))
grafo.insert_arista("Yoda", "Han Solo", randint(1, 20))
grafo.insert_arista("Yoda", "R2.D2", randint(1, 20))
grafo.insert_arista("Yoda", "BB.8", randint(1, 20))

grafo.insert_arista("Boba Fett", "C.3PO", randint(1, 20))
grafo.insert_arista("Boba Fett", "Leiar", randint(1, 20))
grafo.insert_arista("Boba Fett", "Rey", randint(1, 20))
grafo.insert_arista("Boba Fett", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Boba Fett", "Chewbacca", randint(1, 20))
grafo.insert_arista("Boba Fett", "Han Solo", 30) # <---- mdfy
grafo.insert_arista("Boba Fett", "R2.D2", randint(1, 20))
grafo.insert_arista("Boba Fett", "BB.8", randint(1, 20))

grafo.insert_arista("C.3PO", "Leiar", randint(1, 20))
grafo.insert_arista("C.3PO", "Rey", randint(1, 20))
grafo.insert_arista("C.3PO", "Kylo Ren", randint(1, 20))
grafo.insert_arista("C.3PO", "Chewbacca", randint(1, 20))
grafo.insert_arista("C.3PO", "Han Solo", randint(1, 20))
grafo.insert_arista("C.3PO", "R2.D2", randint(1, 20))
grafo.insert_arista("C.3PO", "BB.8", 30)   # <---- mdfy

grafo.insert_arista("Leia", "Rey", randint(1, 20))
grafo.insert_arista("Leia", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Leia", "Chewbacca", randint(1, 20))
grafo.insert_arista("Leia", "Han Solo", randint(1, 20))
grafo.insert_arista("Leia", "R2.D2", randint(1, 20))
grafo.insert_arista("Leia", "BB.8", randint(1, 20))

grafo.insert_arista("Rey", "Kylo Ren", randint(1, 20))
grafo.insert_arista("Rey", "Chewbacca", randint(1, 20))
grafo.insert_arista("Rey", "Han Solo", randint(1, 20))
grafo.insert_arista("Rey", "R2.D2", randint(1, 20))
grafo.insert_arista("Rey", "BB.8", randint(1, 20))

grafo.insert_arista("Kylo Ren", "Chewbacca", randint(1, 20))
grafo.insert_arista("Kylo Ren", "Han Solo", randint(1, 20))
grafo.insert_arista("Kylo Ren", "R2.D2", randint(1, 20))
grafo.insert_arista("Kylo Ren", "BB.8", randint(1, 20))

grafo.insert_arista("Chewbacca", "Han Solo", randint(1, 20))
grafo.insert_arista("Chewbacca", "R2.D2", randint(1, 20))
grafo.insert_arista("Chewbacca", "BB.8", randint(1, 20))

grafo.insert_arista("Han Solo", "R2.D2", randint(1, 20))
grafo.insert_arista("Han Solo", "BB.8", randint(1, 20))

grafo.insert_arista("R2.D2", "BB.8", randint(1, 20))

# barrido

for vertice in grafo.elements:
    print(f"El personaje {vertice["value"]!r} se relaciona con: ")
    for adyacente in vertice["aristas"]:
        print(f" -> {adyacente["value"]!r}, Episodios: {adyacente["peso"]}")


# arbol de expansion minima, tomando a 'Luke Skywalker' como origen

arbol = grafo.kruskal("Luke Skywalker")

print("\nArbol de expansion minima (Origen=Luke Skywalker):")

encontrado = False

print(f"|{"origen":^15}|{"Destino":^15}|{"Peso":^8}|")
for arista in arbol[0].split(';'):
    origen, destino, peso = arista.split('-')
    if (origen == "Yoda" or destino == "Yoda"):
        encontrado = True
        print(f"| {origen:<14}| {destino:<14}| {peso:>6} | *")
    else:
        print(f"| {origen:<14}| {destino:<14}| {peso:>6} |")

if (encontrado):
    print(f"\nYoda esta en el arbol de expansion minima")
else:
    print(f"\nYoda NO esta en el arbol de expansion minima")


# modifica el barrido por amplitud para determinar la arista con mayor peso

def amplitude_show(graf, origin):
    maximos = {"peso": 0, "origen" : [], "destino" : []}
    graf.mark_as_not_visited()
    cola = Queue()
    pos_vertice = graf.search(origin)
    if pos_vertice is not None:
        if not graf.elements[pos_vertice]['visitado']:
            cola.arrive(graf.elements[pos_vertice])
            while cola.size() > 0:
                nodo = cola.attention()
                nodo['visitado'] = True

                adyacentes = nodo['aristas']
                for adyacente in adyacentes:
                    pos_adyaecnte = graf.search(adyacente['value'])

                    if not graf.elements[pos_adyaecnte]['visitado']:

                        # modificacion 😎
                        if (adyacente["peso"] == maximos["peso"]):
                            maximos["origen"].append(nodo["value"])
                            maximos["destino"].append(adyacente["value"])
                        if (adyacente["peso"] > maximos["peso"]):
                            maximos = {"peso": 0, "origen": [], "destino": []}
                            maximos["peso"] = adyacente["peso"]
                            maximos["origen"].append(nodo["value"])
                            maximos["destino"].append(adyacente["value"])

                        cola.arrive(graf.elements[pos_adyaecnte])
    return (maximos)


resultado = amplitude_show(grafo, "Luke Skywalker")


print(f"\nLos personajes que comparten mas episodios son: ")

for indice, arista in enumerate(resultado["origen"]):
    print(f"  PERSONAJES: (Origen={resultado["origen"][indice]}) -> (Destino={resultado["destino"][indice]}), numero de episodios: {resultado["peso"]}")
