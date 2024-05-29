from stack import Stack



def barrido(pila, message="", end=""):
    pila_aux = Stack()  
    print(f"\n{message} Elmentos de la pila: ", end="")
    
    while not (pila.is_empty()):
        elemento = pila.pop()
        print(f" {elemento} ", end=end)
        pila_aux.push(elemento)
    
    while not (pila_aux.is_empty()):
        
        pila.push(pila_aux.pop())
        
    print("")


def ordenar(pila: Stack):
    tmpStack = Stack()
    
    while not (pila.is_empty()):
        tmp = pila.pop()
        
        print(" > ", tmpStack.is_empty())
        input()
        
        while ( (not tmpStack.is_empty()) and tmpStack.top() < tmp ):
            pila.push(tmpStack.pop())
            
        tmpStack.push(tmp)
    
    return tmpStack
        



if __name__=="__main__":
    
    prueba = Stack()
    
    prueba.push(5)
    prueba.push(1)
    prueba.push(3)
    prueba.push(4)
    prueba.push(2)
    prueba.push(6)
    
    barrido(prueba)
    
    print("***")
    
    aux = ordenar(prueba)
    
    barrido(aux, "Pila ordenada: ", "\n")
    
    