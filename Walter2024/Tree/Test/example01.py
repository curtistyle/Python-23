from person import Person, people

ppl = people()

ppl.sort(key=lambda value : value.name)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(numeros[len(numeros)//2:])

def busqueda(lista:list, value):
    #print("medio: ", len(lista)//2)
    if (lista == []):
        return [None]
    elif (value == lista[len(lista)//2]):
        return [lista[len(lista)//2]]
    elif (value > lista[len(lista)//2]):
        #print("a",lista[len(lista)//2:])
        #input()
        return busqueda(lista[len(lista)//2+1:], value)
    else:
        #print("b",lista[:len(lista)//2])
        #input()
        return busqueda(lista[:len(lista)//2], value)
   
nueva = Person("Curtis", "Style", 12, "Urdinarrain")

def hacer(value):
    return value.name

    
for i in range(0,12):
    print("i: ", i, " ",end="")
    print(busqueda(numeros, i))


