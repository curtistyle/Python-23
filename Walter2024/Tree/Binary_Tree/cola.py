class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        """Añade un elemento al final de la cola"""
        self.__elements.append(element)

    def attention(self):
        """Quita y retorna el primer elemento de la cola"""
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        """Numero de elementos actual de la cola"""
        return len(self.__elements)

    def on_front(self):
        """Retorna el primer elemento de la cola"""
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        """Mueve el primer elemento de la cola al final"""
        element = self.attention()
        if element is not None:
            self.arrive(element)