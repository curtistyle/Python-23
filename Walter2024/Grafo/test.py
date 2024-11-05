from grafo import Graph

g = Graph()

g.insert_vertice("A")
g.insert_vertice("B")
g.insert_vertice("C")
g.insert_vertice("D")
g.insert_vertice("E")
g.insert_vertice("F")

g.insert_arista("A", "B", 1)
g.insert_arista("A", "C", 1)
g.insert_arista("A", "D", 1)

g.insert_arista("C", "B", 1)

g.insert_arista("E", "B", 1)

g.insert_arista("F", "B", 1)


def mayor_cantidad_aristas(grap: Graph, salen=True):
    nodos_maximos = []
    mayor = 0
    if (salen):
        for nodo in grap.elements:
            if len(nodo['aristas']) > mayor:
                nodos_maximos.clear()
                nodos_maximos.append(nodo)
                mayor = len(nodo['aristas'])
            elif len(nodo['aristas']) == mayor:
                nodos_maximos.append(nodo)
    else:
        for nodo in grap.elements:
            temp = dict
            for arista in nodo['aristas']:
                temp.update({arista:+1})    
    
    return nodos_maximos

for item in mayor_cantidad_aristas(g):
    print(item)


if (__name__=="__main__"):
    temp = {}
    
    temp.update({"dia":1})
    temp.update({"dia":1})
    temp.update({"dia":1})
    
    print(temp)
    
    