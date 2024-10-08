from Binary_Tree.BinaryTree_ALV_Generic import BinaryTree
from Binary_Tree.cola import Queue

import msvcrt

criaturas = [
    {"nombre":"Ceto", "derrotado_por": None},
    {"nombre":"Tifón", "derrotado_por": "Zeus"},
    {"nombre":"Equidna", "derrotado_por": "Argos Panoptes"},
    {"nombre":"Dino", "derrotado_por": None},
    {"nombre":"Pefredo", "derrotado_por": None},
    {"nombre":"Enio", "derrotado_por": None},
    {"nombre":"Escila", "derrotado_por": None},
    {"nombre":"Caribdis", "derrotado_por": None},
    {"nombre":"Euríale", "derrotado_por": None},
    {"nombre":"Esteno", "derrotado_por": None},
    {"nombre":"Medusa", "derrotado_por": "Perseo"},
    {"nombre":"Ladón", "derrotado_por": "Heracles"},
    {"nombre":"Águila del Cáucaso", "derrotado_por": None},
    {"nombre":"Quimera", "derrotado_por": "Belerofonte"},
    {"nombre":"Hidra de Lerna", "derrotado_por": "Heracles"},
    {"nombre":"Leon de Nemea", "derrotado_por": "Heracles"},
    {"nombre":"Esfinge", "derrotado_por": "Edipto"},
    {"nombre":"Dragon de la Cólquida", "derrotado_por": None},
    {"nombre":"Cerbero", "derrotado_por": None},
    {"nombre":"Cerda de Cromión", "derrotado_por": "Teseo"},
    {"nombre":"Ortro", "derrotado_por": "Heracles"},
    {"nombre":"Toro de Creta", "derrotado_por": "Teseo"},
    {"nombre":"Jabalí de Calidón", "derrotado_por": "Atalanta"},
    {"nombre":"Carcinos", "derrotado_por": None},
    {"nombre":"Gerión", "derrotado_por": "Heracles"},
    {"nombre":"Cloto", "derrotado_por": None},
    {"nombre":"Láquesis", "derrotado_por": None},
    {"nombre":"Átropos", "derrotado_por": None},
    {"nombre":"Minotauro de Creta", "derrotado_por": "Teseo"},
    {"nombre":"Harpías", "derrotado_por": None},
    {"nombre":"Argos Panoptes", "derrotado_por": "Hermes"},
    {"nombre":"Aves del Estínfano", "derrotado_por": None},
    {"nombre":"Talos", "derrotado_por": "Madea"},
    {"nombre":"Sirenas", "derrotado_por": None},
    {"nombre":"Pitón", "derrotado_por": "Apolo"},
    {"nombre":"Cierva de Carinea", "derrotado_por": None},
    {"nombre":"Basilisco", "derrotado_por": None},
    {"nombre":"Jabalí de Erimanto", "derrotado_por": None},
]

tree = BinaryTree()

for criatura in criaturas:
    tree.insert_node(criatura, "nombre")

# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:

# todo: a. listado inorden de las criaturas y quienes la derrotaron;

print(f"\n\033[92m(a) Listado de criatura y quienes las derrotarion\033[00m", end="\n\n")

def mostrar(value):
    print(f"La criatira {value["nombre"]} fue derrotada por {value["derrotado_por"]}")
    return value

tree.select(mostrar, sweep="inorden")

# todo: b. se debe permitir cargar una breve descripción sobre cada criatura;

print(f"\n\033[92m(b) Cargar breve descripcion sebre cada criatura\033[00m", end="\n\n")

def actualizar_todos(value):
    print(f"Agregar una descripcion a la criatura \'{value["nombre"]}\'.")
    descripcion = {"descripcion" : None}
    descripcion["descripcion"] = input("Descripcion: ")
    value.update(descripcion)
    

centinela = True
while(centinela):
    print(f"Cargar una descripcion a una criatura (1), o a todas las criaturas (2), Pasar (0). ")
    opc = msvcrt.getwch()
    if (opc == "1"):
        print("Cambiar la descrpcion de una unica criatura.")
        criatura = input("Ingrese el nombre: ")
        if (tree.search(criatura, key="nombre")):
            descripcion = input(f"Ingrese una descripcion para la criatura \'{criatura}\': ")
            tree.update(criatura, "nombre", {"descripcion" : descripcion})
        else:
            print(f"No se encuentra la criatura.")
    elif (opc == "2"):
        tree.select(actualizar_todos)
    elif (opc == "0"):
        centinela = False
    
tree.inorden()

# TODO : c. mostrar toda la información de la criatura Talos;

print(f"\n\033[92m(c) Toda la informacion de la criatura 'Talos'\033[00m", end="\n\n")

nodo = tree.search("Talos", "nombre")

for key, item in nodo.value.items():
    print(f"{key[0].upper()+key[1:]}=\'{item}\'", end=", ")


# TODO: d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print(f"\n\033[92m(d) Los 3 heroes que derrotaron la mayor cantidad de criaturas\033[00m", end="\n\n")

resultado = tree.group_and_count("derrotado_por")

for index in range(3):
    heroe, c_derrotadas = list(resultado.items())[index]
    print(f"El heroe {heroe} derroto a {c_derrotadas} criaturas.")

# todo: e. listar las criaturas derrotadas por Heracles;

def derrotado_por_heracles(value):
    return value["derrotado_por"] == "Heracles"

print(f"\n\033[92m(e) Criaturas derrotadas por Heracles\033[00m", end="\n\n")

criaturas_derrotadas=tree.where(derrotado_por_heracles) # lista

for criatura in criaturas_derrotadas:
    print(f"# {criatura["nombre"]}")

# todo: f. listar las criaturas que no han sido derrotadas;

print(f"\n\033[92m(f) Criaturas que no fueron derrotadas\033[00m", end="\n\n")

def no_derrotadas(value):
    return value["derrotado_por"] == None

criaturas_no_derrotadas=tree.where(no_derrotadas)

for criatura in criaturas_no_derrotadas:
    print(f"# {criatura["nombre"]}")
    
# todo: g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;

def agregar_captura(value):
    if value["derrotado_por"] == None:
        value["captura"] = input(f" - Agrega el heroe que capturo a \'{value["nombre"]}\': ")
    return value    
print(f"\n\033[92m(g) Agregamos las capturas de cada criatura.\033[00m", end="\n\n")


tree.select(agregar_captura)

# todo: h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;

print(f"\n\033[92m(h) Modificamos los nodos de las criaturas.\033[00m", end="")
print(f"\033[96m Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto.\033[00m", end="")
print(f"\033[92m Indicando que Heravles las atrapo.\033[00m", end="\n\n")


buscados = [
    "Cerbero", 
    "Toro de Creta", 
    "Cierva Cerinea", 
    "Jabalí de Erimanto"
]

for buscado in buscados:
    nodo = tree.search(buscado, "nombre")
    if (nodo is not None):
        nueva_captura = {"captura" : "Heracles"}
        tree.update_any(buscado, "nombre", nueva_captura)
    else:
        tree.insert_node({"nombre":buscado, "derrotado_por": None, "descripcion" : None, "captura": "Heracles"}, "nombre")
        

print("Listado: \n")

tree.inorden()

# todo: i. se debe permitir búsquedas por coincidencia;

print(f"\n\033[92m(i) Busqueda por coincidencia: \033[00m", end="\n\n")

clave = input("Ingrese el criterio/clave de busqueda (nombre [default], derrotado_por, capturado, descripcion): ")

if clave == "":
    buscar = input(f"Ingrese el valor de \'nombre\': ")
    resultados = tree.nearby_search(buscar, "nombre")
else:
    buscar = input(f"Ingrese el valor de \'{clave}\': ")
    resultados = tree.nearby_search(buscar, clave)

print(f"\033[92m Se encontraron {len(resultados)}:\033[00m", end="\n\n")

for item in resultados:
    print(item)

# todo: j. Eliminar al Basilisco y a las Sirenas;

print(f"\n\033[92m(j) Eliminar al \033[00m", end="")
print(f"\033[96m asilisco y a las Sirenas.\033[00m", end="\n\n")

tree.delete_node("Basilisco")

tree.delete_node("Sirenas")

tree.inorden()

# todo: k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;

print(f"\n\033[92m(j) Modificar el nodo que contiene a las Aves del Estínfalo, agregado que Heracles derroto a varias.  \033[00m", end="\n\n")

resultado = tree.search("Aves del Estínfano", "nombre")

if (resultado is not None):
    modificar :dict = resultado.value.copy()
    modificar.pop("nombre")
    modificar["derrotado_por"] = "Heracles"
    modificar["descripcion"] = "Heracles derrota a varias"
    tree.update_any("Aves del Estínfano", "nombre", modificar)
else:
    print("No se encontraron resultados.")

# todo: l. modifique el nombre de la criatura Ladón por Dragón Ladón;

print(f"\n\033[92m(l) Modifica el nombre de la criatura Ladón por Dragón Ladón.  \033[00m", end="\n\n")

resultado = tree.search("Ladón", "nombre")

modificar : dict = resultado.value.copy()
modificar["nombre"] = "Dragón Ladón"

tree.delete_node("Ladón")
tree.insert_node(modificar, "nombre")

tree.inorden()

# todo: m. realizar un listado por nivel del árbol;

print(f"\n\033[92m(m) Listado por nivel del Arbol.  \033[00m", end="\n\n")

tree.by_level()

# todo: n. muestre las criaturas capturadas por Heracles.

print(f"\n\033[92m(n) Criaturas capturadas por Heracles.  \033[00m", end="\n\n")

def capturadas_por_heracle(value:dict):
    if value.get("captura") == "Heracles":
        print(f"Heracles capturo a {value["nombre"]}")
    return value

tree.select(capturadas_por_heracle)


