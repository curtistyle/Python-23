def listar(lista : list):
    if (len(lista) == 0):
        return lista[0]
    else:
        return lista[::-1]
    
if __name__=="__main__":
    myLista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    lista_inversa = listar(myLista)
    print(lista_inversa)