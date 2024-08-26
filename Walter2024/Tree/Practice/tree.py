
class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None) -> None:
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class Arbol():
    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, valor):
        def __insertar_nodo(raiz, valor):
            if raiz is None:
                return Nodo(valor)
            elif (valor < raiz.valor):
                raiz.izquierda = __insertar_nodo(raiz.izquierda, valor)
            else:
                raiz.derecha = __insertar_nodo(raiz.derecha, valor)
            return raiz
        
        self.raiz = __insertar_nodo(self.raiz, valor)

    def preorden(self):
        def __preorden(raiz):
            if raiz is not None:
                print("valor: ", raiz.valor)
                __preorden(raiz.izquierda)
                __preorden(raiz.derecha)

        if self.raiz is not None:
            __preorden(self.raiz)




if __name__=="__main__":

    arbol = Arbol()

    arbol.insertar_nodo(19)
    arbol.insertar_nodo(7)

    arbol.preorden()

""" 
    arbol.insertar_nodo(31)
    arbol.insertar_nodo(11)
    arbol.insertar_nodo(10)
    arbol.insertar_nodo(45)
    arbol.insertar_nodo(22)
    arbol.insertar_nodo(27)
"""