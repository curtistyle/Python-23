from stack import Stack
from stack_methods import barrido
from random import shuffle

lista = [
    {
        "name": "Tony Stark",
        "nickname": "Iron Man",
        "count": 10
    },
    {
        "name": "Steve Rogers",
        "nickname": "Capitan America",
        "count": 8
    },
    {
        "name": "Thor",
        "nickname": None,
        "count": 8
    },
    {
        "name": "Bruce Banner",
        "nickname": "Hulk",
        "count": 7
    },
    {
        "name": "Natasha Romanoff",
        "nickname": "Viuda Negra",
        "count": 7
    },
    {
        "name": "Clint Barton",
        "nickname": "Ojo de Halcón",
        "count": 6
    },
    {
        "name": "Loki",
        "nickname": None,
        "count": 6
    },
    {
        "name": "Peter Parker",
        "nickname": "Spider-Man",
        "count": 3
    },
    {
        "name": "Stephen Strange",
        "nickname": "Doctor Strange",
        "count": 3
    },
    {
        "name": "Carol Danvers",
        "nickname": "Capitana Marvel",
        "count": 2
    },
    {
        "name": "Scott Lang",
        "nickname": "Ant-Man",
        "count": 3
    },
    {
        "name": "Hope van Dyne",
        "nickname": "Avispa",
        "count": 3
    },
    {
        "name": "Peter Quill",
        "nickname": "Star-Lord",
        "count": 3
    },
    {
        "name": "Gamora",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Drax el Destructor",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Rocket Raccoon",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Groot",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Mantis",
        "nickname": None,
        "count": 2
    },
    {
        "name": "Nebula",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Okoye",
        "nickname": None,
        "count": 3
    },
    {
        "name": "M'Baku",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Shuri",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Wong",
        "nickname": None,
        "count": 3
    },
    {
        "name": "Nick Fury",
        "nickname": None,
        "count": 9
    },
    {
        "name": "Maria Hill",
        "nickname": None,
        "count": 5
    }   
    
]


def determinar_posicion(pila : Stack, buscado : str, key: str):
    contador = 0
    encontrado = False
    pila_temp = Stack()
    # ? Quito los items de la cima y lo comparo 
    while ((not pila.is_empty()) and (encontrado == False)):
        if (pila.top()[key] == buscado):
            print("> ",pila.top()[key])
            encontrado = True
        else:
            # ? Los items que quito los guardo en una pila auxiliar, asi no pierdo los datos
            pila_temp.push(pila.pop())
        # ? Cuento las iteraciones
        contador += 1
    # ? Repongo la pila original
    while not pila_temp.is_empty():
        pila.push(pila_temp.pop())
    if not (encontrado):
        contador = -1
    del pila_temp
    return contador
    
def mostrar_peliculas(pila : Stack):
    pila_temp = Stack()
    
    print(f"\n{'name':20} {'nickname':20} {'count':>5}")
    while not pila.is_empty():
        if (pila.top()['count'] >= 5):
            print(f"{pila.top()['name']:20} {str(pila.top()['nickname']):20} {pila.top()['count']:>5}")
        pila_temp.push(pila.pop())
        
    while not pila_temp.is_empty():
        pila.push(pila_temp.pop())
    
    del pila_temp

def buscar_mostrar(pila : Stack, buscado, key : str):
    pila_temp = Stack()
    encontrado = False
    
    print(f"\n{'name':20} {'nickname':20} {'count':>5}")
    while ((not pila.is_empty()) and (encontrado == False)):
        if (pila.top()[key] == buscado):
            print(f"{pila.top()['name']:20} {str(pila.top()['nickname']):20} {pila.top()['count']:>5}")
            encontrado = True
        pila_temp.push(pila.pop())
    
    while not pila_temp.is_empty():
        pila.push(pila_temp.pop())
    
    if not (encontrado):
        print(f"\'{buscado}\' no esta en la pila")
    
    del pila_temp

def buscar_mostrar_por_letra(pila : Stack, key : str, *chars):
    pila_temp = Stack()
    print(f"\n{'name':20} {'nickname':20} {'count':>5}")

    while not (pila.is_empty()):
        if (str(pila.top()[key])[0].lower() in chars):
            print(f"{pila.top()['name']:20} {str(pila.top()['nickname']):20} {pila.top()['count']:>5}")
        pila_temp.push(pila.pop())
    
    while not pila_temp.is_empty():
        pila.push(pila_temp.pop())
    
    del pila_temp
    

if __name__=="__main__":
    pila_personajes = Stack()    
    
    shuffle(lista)
    
    for item in lista:
        pila_personajes.push(item)
        
    barrido(pila_personajes, end="\n")
    
    print("Posicion de Groot: ",determinar_posicion(pila_personajes, "Groot", "name"), end="\n")
    print("Posicion de Groot: ",determinar_posicion(pila_personajes, "Rocket Raccoon", "name"), end="\n")
    
    print("Personajes con 5 o mas participaciones.")
    mostrar_peliculas(pila_personajes)
    
    print("")
    buscar_mostrar(pila_personajes, "Viuda Negra", "nickname")
    
    print("Personajes que empiezan con la letra \'C\', \'D\' y \'G\'")
    print("POR NOMBRE:")
    buscar_mostrar_por_letra(pila_personajes, 'name', "c", "d", "g")
    print("\nPOR APODO:")
    buscar_mostrar_por_letra(pila_personajes, 'nickname', "c", "d", "g")
    
 