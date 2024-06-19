from list import MyList
from pokemon import Pokemon
from coach import Coach


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
                {"name" : "Wurmple", "level" : 62, "type" : "Bicho", "sub_type" : None},
                {"name" : "Wurmple", "level" : 13, "type" : "Bicho", "sub_type" : None}
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
                {"name" : "Fennekin", "level" : 58, "type" : "Fuego", "sub_type" : None},
                {"name" : "Terrakion", "level" : 58, "type" : "Roca", "sub_type" : "Lucha"}
                
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
                {"name" : "Dragonite", "level" : 85, "type" : "Dragón", "sub_type" : "Volador"},
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
                {"name" : "Archeops", "level" : 61, "type" : "Roca", "sub_type" : "Volador"},
                {"name" : "Wingull", "level" : 50, "type" : "Agua", "sub_type" : "Volador"}
                
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

def by_name(value):
    # return value[1]['name']
    return value['name']

def by_tournaments_win(value):
    return value['tournaments_win']



if __name__=="__main__":
    coachs = MyList()
    
    for item in temp_list:
        coach = Coach(
            item["name"], 
            item["tournaments_win"], 
            item["battle_win"], 
            item["battle_lost"],
            MyList())
        for pkm in item["pokemons"]:
            coach.pokemons.append(
                Pokemon(pkm['name'], 
                        pkm["level"], 
                        pkm["type"], 
                        pkm["sub_type"])
                )
        coachs.append(coach)






    # # TODO: (h) determinar cuántos entrenadores tienen a un determinado Pokémon
    
    # print(f"(h) Determina cuantos Entrenadores tiene un determinado Pokemon: ")
    
    # buscado = input("Ingrese el nombre de un Pokemon: ")

    # resultado = MyList()
    
    # for coach in coachs:
    #     count = coach.pokemons.countOcurrencesForKey('name', 'Torterra')
    #     print(f"{coach.name} - {count=}")
        
        
 
        
    # print(f"Son {len(resultado)} los entrenadores que tienen un Pokemon llamado '{buscado}': ")
    # resultado.show()















#     # TODO: (f) mostrar los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
    
#     print(f"(f) Muestra los entrenadores que tengan pokemones de tipo/subtipo : Fuego|Planta|Agua|Volador: ")
    
#     # resultado = MyList()
#     # for index, coach in enumerate(coachs):
#     #     pokemons = coach.pokemons
#     #     for index, pokemon in enumerate(pokemons):
#     #         if (pokemon.type in ["Fuego", "Planta"]) or (pokemon.subtype in ["Agua", "Volador"]) :
#     #             resultado.appendUnique(coach)
                
#     # resultado.showForKeys("name")

#     def es_tipo_o_subtipo(value : Pokemon):
#         return (value.type in ["Fuego" , "Planta"]) or (value.subtype in ["Agua", "Volador"])
    
#     resultado = MyList()
#     for coach in coachs:
#         resultado = coach.pokemons.forEach(function=es_tipo_o_subtipo)   
#         if not resultado.is_emty():
#             print(coach.name)
#             print(resultado)


#     resultado.s



# a = [{"name" : "Carlos"}, {"name" : "Marta"}]
# b = ["Carlos", "Marta"]



# def _is_tda(lyst):
#     """si no es tda"""
#     return type(lyst[0]) in [type(list()), type(object())]

#     # return type(lyst[0]) in [type(str()), type(int()), type(float()), type(complex()), type(bool()), type(bytes()),type(bytearray()), type(str()), type(bytearray())]

# print(_is_not_tda(a))

# print(_is_not_tda(b))



















# class Person():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __repr__(self) -> str:
#         return f"Person(name={self.name}, age={self.age})"
    

# personas = [
#     Person("Curtis", 22),
#     Person("Carlos", 33),
#     Person("Gaspacho", 31),
#     Person("Ana", 20)
# ]

# def es_diccionario(lista : list):
#     return type(lista[0] == type(dict()))

# print(es_diccionario())

# def buscar(lyst, value, key):
#     for index, item in enumerate(lyst):
#         if item.key == value:
#             print(index)
            
# buscar(personas, "Ana", Person.name)

# casa =classmethod()


# setattr(casa, "name", "Carlos")

# # print(casa)
# class Person():
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
        
#     def __repr__(self) -> str:
#         return f"Person(name={self.name}, age={self.age})"


# data = [
#     {"name" : "Carlos", "age" : 20},
#     {"name" : "Curtis", "age" : 18},
#     {"name" : "Marcos", "age" : 24},
#     {"name" : "Ana" , "age" : 17},
#     {"name" : "Sofia", "age" : 20}
# ]

# data_obj = []

# for item in data:
#     data_obj.append(Person(item["name"], item["age"]))

# def mayor_que(value):
#     return value["age"] > 20

# def obj_mayor_que(value):
#     return value.age > 20

# def forEach(data, function):
#     temp = []
#     for index, item in enumerate(data):
#         if function(item):
#             temp.append(item)
#     return temp


# print(forEach(data_obj, function=obj_mayor_que))


# l1 = ["Fuego", "Agua"]

# l2 = ["Volador", "Agua", "Lucha", "Fuego"]

# print(True if (l1[0] or l1[1]) in l2 else False)

