def invertir_cadena(cadena):
    if len(cadena) == 1 or len(cadena) == 0:
        return cadena
    else:
        #print(cadena)
        return cadena[-1] + invertir_cadena(cadena[0:-1])


def operate(lista):
    if (lista == []):
        return lista
    else:
        primero = lista[:1]
        
        return ([lista[:1][0] + 2]) + operate(lista[1:])

    
def operate2(lista1, lista2):
    if lista1 == []:
        return lista1
    else:
        return lista2[:1] + lista1[:1] + operate2(lista1[1:], lista2[1:])

def UpStr(cadena, letra):
    if (len(cadena) == 0):
        return cadena
    else:
        if (cadena[0] == letra):
            return cadena[0].upper() + UpStr(cadena[1:], letra)
        return cadena[0] + UpStr(cadena[1:], letra)

def Pares(lista):
    if (lista == []):
        return [None]
    else:
        if ((lista[0] % 2) == 0):
            return lista[:1] + Pares(lista[1:])
        else:
            return Pares(lista[1:])


def encontrar_elemento(lista, buscado):
    if lista == []:
        return ["No encontrado"]
    elif (lista[0] == buscado):
        return lista[0]
    else:
        return encontrar_elemento(lista[1:], buscado)
        
def encontrar_posicion(lista, buscado, posicion=0):
    if lista == []:
        return -1
    elif (lista[0] == buscado):
        return posicion
    else:
        return encontrar_posicion(lista[1:], buscado, posicion+1)


def busqueda_binaria(lista, buscado):
    #print("MEDIO: ", lista[len(lista)//2])
    if lista==[]:
        return None
    elif (lista[len(lista)//2] == buscado):
        return lista[len(lista)//2];
    elif (buscado > lista[len(lista)//2]):
        #print("a > ",lista[(len(lista)//2)+1:])
        #input()
        return busqueda_binaria(lista[(len(lista)//2)+1:], buscado)
    else:
        #print("b < ",lista[:(len(lista)//2)])
        #input()
        return busqueda_binaria(lista[:(len(lista)//2)], buscado)



if __name__=="__main__":
    lista = [1, 2, 3]
    primero = lista[:1]
    primero = [primero[0] + 2]
    #print(primero)

    print(operate(lista))

    print(operate2([2,4,6], [1,3,5]))

    print(UpStr("sebaats", "a"))

    print("pares: ", Pares([1, 2, 3, 4, 5, 6]))

    print(encontrar_elemento([1,2,4,5,6,7,8,9,0], 0))

    lst = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

    print("Busqueda lineal recursiva: \n")
    buscado="Martes"
    print(f"Buscamos \'{buscado}\': ", encontrar_posicion(lst, buscado))

    aux = [1, 2, 3, 4, 5, 6, 7, 8]
    print("\ntest aux: [aux[ : len(aux)//2]]", aux[:len(aux)//2-1])
    print("\ntest aux: [aux[len(aux)//2 : ]", aux[len(aux)//2:])

    buscado = 6
    print(f"\nBusqueda binaia: [se busca: \'{buscado}\']")    
    lst.sort()
    print(aux)
    print(f"Buscado: \'{buscado}\' : ", busqueda_binaria(aux,buscado))

    # for item in aux:
    #     print(busqueda_binaria(aux,item))
    #     input()