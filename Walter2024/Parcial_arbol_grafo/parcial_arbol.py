from arbol_avl import BinaryTree
# Jolteon, Lycanroc y Tyrantrum;
pokemones = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["Fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
    {"nombre": "Jigglypuff", "numero": 39, "tipo": ["Normal", "Hada"]},
    {"nombre": "Meowth", "numero": 52, "tipo": ["Normal"]},
    {"nombre": "Psyduck", "numero": 54, "tipo": ["Agua"]},
    {"nombre": "Machop", "numero": 66, "tipo": ["Lucha"]},
    {"nombre": "Geodude", "numero": 74, "tipo": ["Roca", "Tierra"]},
    {"nombre": "Magnemite", "numero": 81, "tipo": ["Eléctrico", "Acero"]},
    {"nombre": "Gastly", "numero": 92, "tipo": ["Fantasma", "Veneno"]},
    {"nombre": "Onix", "numero": 95, "tipo": ["Roca", "Tierra"]},
    {"nombre": "Eevee", "numero": 133, "tipo": ["Normal"]},
    {"nombre": "Snorlax", "numero": 143, "tipo": ["Normal"]},
    {"nombre": "Dratini", "numero": 147, "tipo": ["Dragón"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["Eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["Roca"]},
]


arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# a. insercion de datos

for pokemon in pokemones:
    # ARBOL NOMBRE
    arbol_nombre.insert_node(pokemon["nombre"], pokemon)
    #ARBOL NUMERO
    arbol_numero.insert_node(pokemon["numero"], pokemon)
    # ARBOL TIPO
    for tipo in pokemon['tipo']:
        arbol_tipo.insert_node(tipo, pokemon)


# b.
# Mostrar datos de un pokemos en especifico

print(f"Busqueda exacta de un pokemon por su numero.\n")

# buscado = int(input("Ingrese el numero del pokemon que deseas buscar: "))
buscado = 74

resultado = arbol_numero.search(buscado)

if resultado is not None:
    print(f"¡ Pokemon encontrado !")
    print(f"* Nombre: {resultado.other_value["nombre"]!r}, Numero: {resultado.other_value["numero"]!r} Tipo: {", ".join(resultado.other_value["tipo"])}.")
else:
    print(f"El pokemon con el numero {buscado} no se encontro!")


# busqueda de proximidad

print("\nBusqueda por priximidad de un pokemon por su nombre: ")

# buscado = input("Ingrese el nombre del pokemon que desea buscar o una referencia: ")

buscado = "M"

print(f"\nSe busco = {buscado!r}, resultado:")

arbol_nombre.proximity_search(buscado) # modifique el proximity_search de la clase Binary_Search para que muestre todos los datos


# c.

# modifico un barrido in-orden para mostrar los pokemos por tipo

def mostrar_todo(tree):
    def __mostrar_todo(root, anterior):
        if root is not None:
            __mostrar_todo(root.left, anterior)

            if (anterior == ""):
                anterior = root.value
            if (anterior != root.value):
                print(f"Tipos {root.value}")
                anterior = root.value
            print(f"  * Nombre: {root.other_value["nombre"]!r}, Numero: {root.other_value["numero"]!r}, Tipos={", ".join(root.other_value["tipo"])!r}")
            __mostrar_todo(root.right, anterior)

    if tree.root is not None:
        __mostrar_todo(tree.root, anterior="")

# todo el listado

print(f"\nMostrando todos los tipos: \n")
mostrar_todo(arbol_tipo)

# mostrar por tipo

def mostrar_por_tipo(tree, tipo):
    def __mostrar_por_tipo(root, tipo):
        if root is not None:
            __mostrar_por_tipo(root.left, tipo)

            if (tipo == root.value):
                print(f"  -> Nombre: {root.other_value["nombre"]!r}, Numero: {root.other_value["numero"]!r}, Tipos={", ".join(root.other_value["tipo"])!r}")
            __mostrar_por_tipo(root.right, tipo)

    if tree.root is not None:
        __mostrar_por_tipo(tree.root, tipo)

tipo = "Agua"

print(f"\n\nTodos los pokemes de tipo {tipo}: ")
mostrar_por_tipo(arbol_tipo, tipo)


# listado inorden (asendente) por nombre y numero de pokemones

print(f"\nListado Ascendente por NOMBRE: \n")

arbol_nombre.inorden()

print(f"\nListado Ascendente por NUMERO: \n")

arbol_numero.inorden()

print(f"\nBarrido por nivel por NOMBRE: \n")

arbol_nombre.by_level()

# mostrar los datos de los pokemones Jolteon, Lycanroc y Tyrantrum;

resultados = [
    arbol_nombre.search("Jolteon"),
    arbol_nombre.search("Lycanroc"),
    arbol_nombre.search("Tyrantrum")
]

print(f"\nSe encontraron los siguientes pokemon's: ")
for res in resultados:
    if res is not None:
        print(f"Nombre: {res.other_value["nombre"]!r}, Numero: {res.other_value["numero"]!r}, {res.other_value["tipo"]!r}")

# mostrar cuantos pokemos hay de tipo electrico y acero
# modificamos un inorden

def contar_tipos(tree, tipos):
    temp = {}

    def __contar_tipos(root, tipos):
        if root is not None:
            __contar_tipos(root.left, tipos)

            if (root.value in tipos):
                if not root.value in temp.keys():
                    temp[root.value] = 0
                temp[root.value] += 1
            __contar_tipos(root.right, tipos)

    if tree.root is not None:
        __contar_tipos(tree.root, tipos)

    return temp

resultado = contar_tipos(arbol_tipo, ["Eléctrico", "Acero"])

print("\nCantidad de pokemons de tipo acero y electrico: \n")
for clave, valor in resultado.items():
    print(f"tipo: {clave!r}, cantidad: {valor!r}")