from list import MyList

temp_list = [
    {
        "name" : "Ash Ketchup",
        "tournaments_win" : 7,
        "battle_win" : 517,
        "battle_lost" : 35,
        "pokemons":
            [
                {"name" : "Charizard", "level" : 94, "type" : "Fuego", "sub_type" : "Volador"},
                {"name" : "Greninja", "level" : 88, "type" : "Agua", "sub_type" : "Siniestro"},
                {"name" : "Lucario", "level" : 75, "type" : "Lucha", "sub_type" : "Acero"},
                {"name" : "Pikachu", "level" : 100, "type" : "Electrico", "sub_type" : None},
                {"name" : "Garchomp", "level" : 70, "type": "Dragón", "sub_type" : "Tierra"},
                {"name" : "Squirtle", "level" : 65, "type" : "Agua", "sub_type" : None}
            ]

    },
    {
        "name" : "Misty",
        "tournaments_win" : 2,
        "battle_win" : 289,
        "battle_lost" : 24,
        "pokemons" : 
            [
                {"name" : "Staryu", "level" : 85, "type" : "Agua", "sub_type" : "Psíquico"},
                {"name" : "Psyduck", "level" : 78, "type" : "Agua", "sub_type" : None},
                {"name" : "Goldeen", "level" : 70, "type" : "Agua", "sub_type" : None},
                {"name" : "Horsea", "level" : 65, "type" : "Agua", "sub_type" : None},
                {"name" : "Seadra", "level" : 60, "type" : "Agua", "sub_type" : None},
                {"name" : "Lapras", "level" : 55, "type" : "Agua", "sub_type" : "Hielo"}
            ]
    },
    {
        "name" : "Brock",
        "tournaments_win" : 5,
        "battle_win" : 278,
        "battle_lost" : 21,
        "pokemons" : 
            [
                {"name" : "Geodude", "level" : 90, "type" : "Roca", "sub_type" : "Tierra"},
                {"name" : "Onix", "level" : 82, "type" : "Roca", "sub_type" : "Tierra"},
                {"name" : "Rhyhorn", "level" : 75, "type" : "Tierra", "sub_type" : "Roca"},
                {"name" : "Steelix", "level" :68, "type" : "Roca", "sub_type" : "Tierra"},
                {"name" : "Golem", "level" : 63, "type" : "Roca", "sub_type" : "Tierra"},
                {"name" : "Sudowoodo", "level" : 58, "type" : "Roca", "sub_type" : None}
            ]
    },
    {
        "name" : "May",
        "tournaments_win" : 3,
        "battle_win" : 261,
        "battle_lost" : 26,
        "pokemons" : 
            [
                {"name" : "Blaziken", "level" : 95, "type" : "Fuego", "sub_type" : "Lucha"},
                {"name" : "Grovlye", "level" : 87, "type" : "Planta", "sub_type" : None},
                {"name" : "Marshtomp", "level" : 79, "type" : "Agua", "sub_type" : "Tierra"},
                {"name" : "Beautifly", "level" : 72, "type" : "Bicho", "sub_type" : "Volador"},
                {"name" : "Combusken", "level" : 67, "type" : "Fuego", "sub_type" : "Lucha"},
                {"name" : "Wurmple", "level" : 62, "type" : "Bicho", "sub_type" : None}
            ]
    },
    {
        "name" : "Dawn",
        "tournaments_win" : 4,
        "battle_win" : 252,
        "battle_lost" : 23,
        "pokemons" : 
            [
                {"name" : "Mamoswine", "level" : 92, "type" : "Hielo", "sub_type" : "Tierra"},
                {"name" : "Togekiss", "level" : 84, "type" : "Hada", "sub_type" : "Volador"},
                {"name" : "Garchomp", "level" : 76, "type" : "Dragón", "sub_type" : "Tierra"},
                {"name" : "Guilava", "level" : 70, "type" : "Fuego", "sub_type" : None},
                {"name" : "Torterra", "level" : 65, "type" : "Planta", "sub_type" : "Tierra"},
                {"name" : "Piplup", "level" : 60, "type" : "Agua", "sub_type" : None}
            ]
    },
    {
        "name" : "Serena",
        "tournaments_win" : 1,
        "battle_win" : 237,
        "battle_lost" : 20,
        "pokemons" :
            [
                {"name" : "Sylveon", "level" : 90, "type" : "Hada", "sub_type" : None},
                {"name" : "Braixen", "level" : 82, "type" : "Fuego", "sub_type" : None},
                {"name" : "Delphox", "level" : 75, "type" : "Fuego", "sub_type" : "Psíquico"},
                {"name" : "Pancham", "level" : 68, "type" : "Lucha", "sub_type": None},
                {"name" : "Madibuzz", "level" : 63, "type" : "Hada", "sub_type" : "Siniestro"},
                {"name" : "Fennekin", "level" : 58, "type" : "Fuego", "sub_type" : None}
            ]
    },
    {
        "name" : "Gary Oak",
        "tournaments_win" : 4,
        "battle_win" : 312,
        "battle_lost" : 17,
        "pokemons" : 
            [
                {"name" : "Blastoide", "level" : 100, "type" : "Agua", "sub_type" : None},
                {"name" : "Charizard", "level" :95, "type" : "Fuego", "sub_type" : "Volador"},
                {"name" : "Alakazam", "level" : 90, "type" : "Psíquico", "sub_type" : None},
                {"nmae" : "Dragonite", "level" : 85, "type" : "Dragón", "sub_type" : "Volador"},
                {"name" : "Rhydon", "level" : 80, "type" : "Tierra", "sub_type" : "Roaca"},
                {"name" : "Arcanine", "level" : 75, "type" : "Fuego", "sub_type" : "None"}
            ]
    },
    {
        "name" : "Paul",
        "tournaments_win" : 2,
        "battle_win" : 248,
        "battle_lost" : 23,
        "pokemons" : 
            [
                {"name" : "Torterra", "level" : 98, "type" : "Planta", "sub_type" : "Tierra"},
                {"name" : "Electivire", "level" : 89, "type" : "Electrico", "sub_type" : None},
                {"name" : "Drapion", "level" : 81, "type" : "Veneno", "sub_type" : "Siniestro"},
                {"name" : "Ursaring", "level" : 74, "type" : "Normal", "sub_type" : None},
                {"name" : "Glalie", "level" : 67, "type" : "Hielo", "sub_type" : None},
                {"name" : "Aggron", "level" : 62, "type" : "Roca", "sub_type" : "Acero"}
            ]
    },
    {
        "name" : "Iris",
        "tournaments_win" : 3,
        "battle_win" : 248,
        "battle_lost" : 29,
        "pokemons" : 
            [
                {"name" : "Haxorus", "level" : 96, "type" : "Dragón", "sub_type" : None},
                {"name" : "Dragapult", "level" : 88, "type" : "Dragón", "sub_type" : "Fantasma"},
                {"name" : "Lapras", "level" : 80, "type" : "Agua", "sub_type" : "Hielo"},
                {"name" : "Salamence", "level" : 73, "type" : "Dragón", "sub_type" : "Psíquico"},
                {"name" : "Exeggucure", "level" : 66, "type" : "Planta" , "sub_type" : "Psíquico"},
                {"name" : "Archeops", "level" : 61, "type" : "Roca", "sub_type" : "Volador"}
            ] 
    },
    {
        "name" : "Gladion",
        "tournaments_win" : 1,
        "battle_win" : 265,
        "battle_lost" : 22,
        "pokemons" :
            [
                {"name" : "Silvally", "level" : 100, "type" : "Hada", "sub_type" : None},
                {"name" : "Umbreon", "level" : 87, "type" : "Siniestro", "sub_type" : None},
                {"name" : "Lycanroc", "level" : 80, "type" : "Roca", "sub_type" : None},
                {"name" : "Poipole", "level" : 73, "type" : "Veneno", "sub_type" : None},
                {"name" : "Zoroark", "level" : 68, "type" : "Siniestro" , "sub_type" : None },
                {"name" : "Sharpeo", "level" :66, "type" : "Agua", "sub_type" : "Siniestro"}
            ]
    }
]

# ? implementaciones
def showDict(value, *keys):
    for index, key in enumerate(keys):
        print(f"'{key}' = {value[key]}, ", end="") if (index < (len(keys) - 1)) else print(f"'{key}' = {value[key]}. ", end="")
    print()





if __name__=="__main__":
    coachs = MyList(temp_list)
    
    # TODO: (a) Obtener la cantidad de pokemones de un entrenador.
    buscado = input("Ingrese el nombre de un pokemos: ")  
    
    posicion = coachs.search("name", buscado)
    
    if not (posicion == -1):
        coach = coachs.getNode(posicion)
        print(f'El entrenador {coach["name"]} tiene {len(coach["pokemons"])}.')
    else:
        print(f"El entrenador '{buscado}' no esta en la lista.")
    
    # TODO: (b) listar los entrenadores que hayan ganado más de tres torneos;
    
    # ! METODO 1:
    print("Entrenadores que han ganado mas de tres torneos (METODO 1):")
    lista_resultado = MyList(filter(lambda x : x['tournaments_win'] > 3, coachs))
    print(f"Los entrenadores con mas de 3 torneos ganados son: ")
    lista_resultado.showForKeys("name", "tournaments_win")
    
    # ! METODO 2:
    print("Entrenadores que han ganado mas de tres torneos (METODO 2):")
    for coach in coachs:
        if (coach["tournaments_win"] > 3):
            showDict(coach, "name", "tournaments_win")
        

    # TODO: (c) el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
    # ! METODO 1:
    print(f"(METODO 1) El pokemon con mayor nivel del entrenador con mas torneos ganados es : ")
    index_coach = coachs.maxForKey("tournaments_win")
    showDict(coachs.getNode(index_coach), "name", "tournaments_win")
    
    pokemons = coachs.getSubList(index_coach, "pokemons")
    index_pokemon = pokemons.maxForKey("level")
    showDict(pokemons.getNode(index_pokemon), "name", "level", "type")
    

    
    
    # ! METODO 2:
    print(f"(METODO 2) El pokemon con mayor nivel del entrenador con mas torneos ganados es: ")
    max_win = 0
    for index, coach in enumerate(coachs):
        if (coach["tournaments_win"] > max_win):
            posicion = index
            max_win = coach["tournaments_win"]
    
    coach = coachs.getNode(posicion)
    showDict(coach, "name", "tournaments_win")
    
    max_level = 0
    pokemons = coach['pokemons']
    for index, pokemon in enumerate(pokemons):
        if (pokemon['level'] > max_level):
            posicion = index
            max_level = pokemon['level']
    
    pokemon = coach["pokemons"][posicion]
    showDict(pokemon, "name", "level", "type")
    
    
    
    