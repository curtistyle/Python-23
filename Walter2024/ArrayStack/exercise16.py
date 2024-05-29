from stack import Stack
from stack_methods import barrido
from random import Random, shuffle

# ! Lista con personajes del episodio "V - The Empire Strikes Back"
lista_1 = [
    {"name": "Luke Skywalker", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "Princesa Leia Organa", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "Han Solo", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "Chewbacca", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "C-3PO", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "R2-D2", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "Yoda", "category": "Héroe", "episode" : "V - The Empire Strikes Back"},
    {"name": "Darth Vader", "category": "Villano", "episode" : "V - The Empire Strikes Back"},
    {"name": "Boba Fett", "category": "Villano", "episode" : "V - The Empire Strikes Back"},
    {"name": "Almirante Ozzel", "category": "Villano", "episode" : "V - The Empire Strikes Back"},
    {"name": "General Veers", "category": "Villano", "episode" : "V - The Empire Strikes Back"},
    {"name": "Droids", "category": "Otros", "episode" : "V - The Empire Strikes Back"},
    {"name": "Refugiados", "category": "Otros", "episode" : "V - The Empire Strikes Back"},
    {"name": "Mon Calamari", "category": "Otros", "episode" : "V - The Empire Strikes Back"},
    {"name": "Sullustans", "category": "Otros", "episode" : "V - The Empire Strikes Back"},
]

lista_2 = [
    {"name": "Rey", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Finn", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Poe Dameron", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Han Solo", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Chewbacca", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Leia Organa", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "C-3PO", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "BB-8", "category": "Héroe", "episode" : "VII - The Force Awakens"},
    {"name": "Kylo Ren", "category": "Villano", "episode" : "VII - The Force Awakens"},
    {"name": "General Hux", "category": "Villano", "episode" : "VII - The Force Awakens"},
    {"name": "Capitán Phasma", "category": "Villano", "episode" : "VII - The Force Awakens"},
    {"name": "Snoke", "category": "Villano", "episode" : "VII - The Force Awakens"},
    {"name": "Maz Kanata", "category": "Otros", "episode" : "VII - The Force Awakens"},
    {"name": "Lor San Tekka", "category": "Otros", "episode" : "VII - The Force Awakens"},
    {"name": "Takeda", "category": "Otros", "episode" : "VII - The Force Awakens"},
    {"name": "Bala-Tik", "category": "Otros", "episode" : "VII - The Force Awakens"},
]


def rename_episode(value : dict):
    value["episode"] = f"\'V - The Empire Strikes Back\' & \'VII - The Force Awakens\'"
    return value

def interseccion(pila_1 : Stack, pila_2 : Stack, key : str) -> Stack:
    pila_aux = Stack()
    pila_interseccion = Stack()
    while not pila_2.is_empty():
        
        while not (pila_1.is_empty()):
            if (pila_1.top()[key] == pila_2.top()[key]):
                rename_episode(pila_1.top())
                pila_interseccion.push(pila_1.pop())
            else:
                pila_aux.push(pila_1.pop())
        pila_2.pop()
        
        while not (pila_aux.is_empty()):
            if (pila_aux.top()[key] == pila_2.top()[key]):
                rename_episode(pila_aux.top())
                pila_interseccion.push(pila_aux.pop())
            else:
                pila_1.push(pila_aux.pop())
        pila_2.pop()
        
    return pila_interseccion

if __name__=="__main__":
    
    # ? Mesclo las listas
    shuffle(lista_1)
    shuffle(lista_2)


    # * Creo las pilas para almacenar los personajes
    episodio_v = Stack()
    episodio_vii = Stack()

    # * Cargo la pila 'episodio_v'
    for item in lista_1:
        episodio_v.push(item)

    # * Cargo la pila 'episodio_vii'
    for item in lista_2:
        episodio_vii.push(item)
    
    # * Determino la interseccion de las dos pilas y la guardo en una nueva pila
    nueva_pila = interseccion(episodio_v, episodio_vii, 'name')
    
    # * Muestro la pila
    barrido(nueva_pila, end="\n")