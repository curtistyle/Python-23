from random import randint, choice, shuffle


""" Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
que contemple las siguientes actividades: 

a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; """

tabla_tipo = {}
tabla_digito = {}
tabla_nivel = {}

def hash_tipo(pokemon):
    return pokemon['tipo']

def hash_digito(pokemon):
    return pokemon['numero'] % 10

def hash_nivel(pokemon):
    return pokemon['nivel'] % 10

# ? (a)
def cargar(t_tipo, t_digito, t_nivel, pokemons : list):

    for pokemon in pokemons:
        # * Tabla Tipo
        tipo = hash_tipo(pokemon)
        if tipo not in t_tipo:
            t_tipo[tipo] = []
        t_tipo[tipo].append(pokemon)

        # * Evalua los subtipos
        subtipo = pokemon['subtipo']
        if subtipo not in tabla_tipo and (subtipo != None):
            tabla_tipo[subtipo] = []
        if subtipo != None:
            tabla_tipo[subtipo].append(pokemon)
        
        # * Tabla digitos
        digito = hash_digito(pokemon)
        if digito not in t_digito:
            t_digito[digito] = []
        t_digito[digito].append(pokemon)
        
        # * Tabla nivel
        nivel = hash_nivel(pokemon)
        if nivel not in t_nivel:
            t_nivel[nivel] = []
        t_nivel[nivel].append(pokemon)  
    

def mostrar_tabla(value : dict):
    for key, items in value.items():
        print(f"{key}:")
        for item in items:
            print(f"    {item}")
        print()

def mostrar_lista(values : list):
    if values is not None:
        for index, item in enumerate(values):
            print(f"{index} :  {item}\n")
    else:
        print(f"No hay pokemones.")
    print()

    
if __name__=="__main__":

    pokemones = [
        {"nombre": "Bulbasaur", "tipo": "Planta", "subtipo": "Hierba", "nivel": 5, "numero": 1},
        {"nombre": "Ivysaur", "tipo": "Planta", "subtipo": "Hierba", "nivel": 16, "numero": 2},
        {"nombre": "Venusaur", "tipo": "Planta", "subtipo": "Hierba", "nivel": 32, "numero": 3},
        {"nombre": "Charmander", "tipo": "Fuego", "subtipo": None, "nivel": 44, "numero": 4},
        {"nombre": "Charmeleon", "tipo": "Fuego", "subtipo": None, "nivel": 16, "numero": 5},
        {"nombre": "Charizard", "tipo": "Fuego", "subtipo": "Volador", "nivel": 36, "numero": 6},
        {"nombre": "Squirtle", "tipo": "Agua", "subtipo": None, "nivel": 5, "numero": 7},
        {"nombre": "Wartortle", "tipo": "Agua", "subtipo": None, "nivel": 16, "numero": 8},
        {"nombre": "Blastoise", "tipo": "Agua", "subtipo": None, "nivel": 36, "numero": 11},
    ]


    cargar(tabla_tipo, tabla_digito, tabla_nivel, pokemones)

    print(" >>  BEFORE << ")    

    print(" >>> TABLA TIPO: ")
    mostrar_tabla(tabla_tipo)
        
    print(" >>> TABLA DIGITO")    
    mostrar_tabla(tabla_digito)
        
    print(" >>> TABLA NIVEL")    
    mostrar_tabla(tabla_nivel)

    print(" >> (d) AFTER (con nuevos pokemones) << ")    

    nuevos_pokemones =[
        {"nombre": "Curtis", "tipo": "Siniestro", "subtipo": "Papeto", "nivel": 40, "numero": 13},
        {"nombre": "Snorlax", "tipo": "Normal", "subtipo": None, "nivel": 25, "numero": 143},
        {"nombre": "Eevee", "tipo": "Normal", "subtipo": None, "nivel": 5, "numero": 133},
        {"nombre": "Pikachu", "tipo": "Electrico", "subtipo": None, "nivel": 5, "numero": 25}
    ]

    cargar(tabla_tipo, tabla_digito, tabla_nivel, nuevos_pokemones)

    print(" >>> TABLA TIPO: ")
    mostrar_tabla(tabla_tipo)
        
    print(" >>> TABLA DIGITO")    
    mostrar_tabla(tabla_digito)
        
    print(" >>> TABLA NIVEL")    
    mostrar_tabla(tabla_nivel)

    # todo: (e) mostrar todos los pokemones cuyos numeros terminan en 3, 7 y 9
    
    print(f"(e) Pokemones cuyos numeros terminan en 3, 7 y 9. \n")
    
    pokemones_3 = tabla_digito.get(3)
    print("Pokemones que terminan con el numero 3:")
    mostrar_lista(pokemones_3)
    
    pokemones_7 = tabla_digito.get(7)
    print("Pokemones que terminan con el numero 7:")
    mostrar_lista(pokemones_7)
    
    pokemones_9 = tabla_digito.get(9)
    print("Pokemones que terminan con el numero 9:")
    mostrar_lista(pokemones_9)
    
    # todo: (f) Mostrar todos los pokemones cuyos niveles son multiplos de 2, 5 y 10
    
    print("(f) Muestra todos los pokemones cuyos nuveles son multiplo de 2, 5 y 10.\n")

    multiplos_de = (2, 5, 10)
    for m in multiplos_de:
        print(f"Multiplo de '{m}': ")
        divisible = [x for x in range(10) if x % m == 0] 
        for d in divisible:
            pokemones = tabla_nivel.get(d)
            mostrar_lista(pokemones)
    
    # print("# MULTIPLOS DE 2: ")
    # multiplos_2 = (0, 2, 4, 6, 8)
    # for m in multiplos_2:
    #     pokemones = tabla_nivel.get(m)
    #     mostrar_lista(pokemones)
        
    # print("# MULTIPLOS DE 3: ")
    # multiplos_5 = (0, 5)
    # for m in multiplos_5:
    #     pokemones = tabla_nivel.get(m)
    #     mostrar_lista(pokemones)
        
    # print("# MULTIPLOS DE 10: ")
    # pokemones = tabla_nivel.get(0)
    # mostrar_lista(pokemones)
        
    # todo: (g) mostrar todos los pokemones de los siguientes tipo: Acero, Fuego, electrico y hielo
    
    print("(g) Muestra todos los pokemones de los siguientes tipos: ")
    
    buscar_tipos = ["Acero", "Fuego", "Electrico", "Hielo"]
    
    for tipos in buscar_tipos:
        lista_buscado = tabla_tipo.get(tipos)
        print(f"Tipos {tipos} \n     ")
        mostrar_lista(lista_buscado)
        
    