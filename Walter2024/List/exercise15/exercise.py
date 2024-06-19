from list import MyList
from pokemon import Pokemon
from coach import Coach
from list_of_pokemons import temp_list

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
    
    
    # TODO: (a) Obtener la cantidad de pokemones de un entrenador.
    
    print("(a) Obtiene la cantidad de pokemones de un entrenados.")
    buscado = input("Ingrese el nombre de un Entrenador: ")
    posicion = coachs.search(buscado, "name")

    if not (posicion == -1):
        coach : Coach = coachs.getNode(posicion)
        print(f'El entrenador {coach.name} tiene {len(coach.pokemons)}.')
    else:
        print(f"El entrenador '{buscado}' no esta en la lista.")
    
    # TODO: (b) listar los entrenadores que hayan ganado más de tres torneos;
    
    print("\n(b) Entrenadores que han ganado mas de tres torneos:")
    
    def mayor_que(value : Coach):
        return value.tournaments_won > 3
    
    resultado = coachs.forEach(function=mayor_que)
    resultado.showForKeys("name", "tournaments_won")
        

    # TODO: (c) mostrar el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
    
    posicion_coach = coachs.max("tournaments_won")
    coach = coachs.getNode(posicion_coach)
    posicion_pokemon =  coach.pokemons.max("level")
    pokemon : Pokemon = coach.pokemons.getNode(posicion_pokemon)
    
    print(f"\n(c) El pokemon de mayor nivel del entrenador con mas torneos ganados es: ")
    print(f"    > Entrenador: {coach.name}")
    print(f"    > Pokemon: {pokemon}")
    

    # TODO: (d) mostrar todos los datos de un entrenador y sus Pokémos;
    
    print("\n(d) Muestra todos los datos de un entrenador y sus Pokémos.")
    buscado = input("Ingrese el nombre de un entrenador: ")
    
    posicion = coachs.search(buscado, "name")
    if not (posicion == -1):
        coach = coachs.getNode(posicion)
        print(f"{coach}")
    else:
        print(f"El entrenador {buscado} no existe en la lista.")
    
    # TODO: (e) mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
    
    # * criterio
    def winrate(win, loss):
        total = win + loss
        res = (win * 100) / total
        return res
    
    def winratePorBatalla(value : Coach):
        return winrate(value.battles_won, value.battles_losses) > 79
    
    resultado = coachs.forEach(function=winratePorBatalla)
    
    print(f"\n(e) Entrenadores cuyo porcentaje de battalla es mayor al 79%: ")
    
    resultado.showForKeys("name", "battles_won", "battles_losses")
    
    # TODO: (f) mostrar los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
    
    print(f"\n(f) Muestra los entrenadores que tengan pokemones de tipo/subtipo : Fuego|Planta|Agua|Volador: ")
    
    # * criterio
    def es_tipo_o_subtipo(value : Pokemon):
        return (value.type in ["Fuego" , "Planta"]) or (value.subtype in ["Agua", "Volador"])
    
    resultado = MyList()
    for coach in coachs:
        resultado = coach.pokemons.forEach(function=es_tipo_o_subtipo)   
        if not resultado.is_emty():
            print(coach.name)
            print(resultado)
    
    # TODO: (g) el promedio de nivel de los Pokémons de un determinado entrenador;
    
    print("\n(g) Promedio de nivel de los Pokemones de un determinado entrenador.")
    buscado = input(f"Ingrese el nombre de un Entreneador: ")
    
    posicion = coachs.search(buscado, "name")
    if posicion != -1:
        coach  = coachs.getNode(posicion)
        print(f"Promedio de nival de los de pokemones del Entrenador: '{coach.name}': ", end="")
        print(f"{coach.pokemons.AverageCalculator('level'):.2f}")
    else:
        print(f"El Entrenador '{buscado}' no esta en lista Lista.")
    
    
    # TODO: (h) determinar cuántos entrenadores tienen a un determinado Pokémon
    
    print(f"\n(h) Determina cuantos Entrenadores tiene un determinado Pokemon: ")
    
    buscado = input("Ingrese el nombre de un Pokemon: ")

    resultado = MyList()
    
    for coach in coachs:
        posicion = coach.pokemons.search(buscado, "name")
        if (posicion != -1):
            resultado.append(coach)
 
    print(f"Son {len(resultado)} los entrenadores que tienen un Pokemon llamado '{buscado}': ")
    resultado.show()
    
    # todo: (i) mostrar los entrenadores que tienen Pokémons repetidos;
    
    print(f"\n(i) Miestra los entrenedores que tienen pokemones repetidos: ")
    
    for coach in coachs:
        resultado = coach.pokemons.getDuplicates("name")
        if (resultado != []):
            print(f"Entrenador: {coach.name}, Pokemones repetidos: ")
            resultado.show()
        
    # todo: (j) Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
    
    print(f"\n(j) Determina los entrenadores que tengan uno de los siguientes polemones 'Tyrantrum|Terrakion|Wingull': ")
    
    pokemones = ["Tyrantrum", "Terrakion", "Wingull"]
    
    for coach in coachs:
        resultado = coach.pokemons.getOccurrences("name", pokemones)
        if (resultado != []):
            print(coach.name)
            print(resultado)
            

    # todo: (k) determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
    
    buscado = {"entrenador" : None, "pokemon" : None}
    
    print(f"\n(k) Determina si un Entrenador 'x' tiene un Pokemon 'y'.")
    
    buscado["entrenador"] = input("Ingrese el nombre de un entrenador: ")
    buscado["pokemon"] = input("Ingrese el nombre del pokemon: ")
    
    posicion_entrenador =  coachs.search(buscado["entrenador"], "name")
    print(f"El entrenador \'{buscado['entrenador']}\'", end="")
    if (posicion_entrenador != -1):
        print(f" esta en la lista.", end="")
        entrenador : Coach = coachs.getNode(posicion_entrenador)
        posicion_pokemon = entrenador.pokemons.search(buscado['pokemon'], "name")
        if (posicion_pokemon != -1):
            print(f" Y contiene al pokemon \'{buscado['pokemon']}\'.")
            print(f"...mas informacion : \n    {coachs.getNode(posicion_entrenador)}")
        else:
            print(f" Pero no contiene al pokemon \'{buscado['pokemon']}\'.")
    else:
        print(f" no esta en la lista.")
        