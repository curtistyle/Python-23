class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izquierda = izq
        self.derecha = der

class Arbol:
    def __init__(self) -> None:
        self.raiz = None

    def insertar_nodo(self, dato):
        if (self.raiz == None):
            self.raiz = Nodo(dato)
        elif (dato < self.raiz.valor):
            self.raiz.izquierda = self.insertar_nodo(self.raiz.izquierda.valor)
        else:
            self.raiz.derecha = self.insertar_nodo(self.raiz.derecha.valor)
        
    


if __name__=="__main__":
    arbol = Arbol()

    arbol.insertar_nodo(1)
    arbol.insertar_nodo(2)
    arbol.insertar_nodo(3)