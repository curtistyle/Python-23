from Binary_Tree.BinaryTree_Generic import BinaryTree

tree = BinaryTree()

personas = [
    {"name":"Curtis", "city":"Urdinarrain"},
    {"name":"Marcos", "city":"Gualeguaychu"},
    {"name":"Carlos", "city":"Parera"},
    {"name":"Matilda", "city":"Aldea San Antonio"},
    {"name":"Alejo", "city":"Aldea San Juan"},
    {"name":"Mario", "city":"Federacion"},
    {"name":"Martin", "city":"Rosario"},
]

for persona in personas:
    tree.insert_node(persona, key="name")

def show(value):
    print(value["name"] + " es de " + value["city"])
    return value
    

# tree.select(show, "posorden")

# resultado = tree.nearby_search("mar", "name")

# for index, item in enumerate(resultado):
#     print(index, " - ",item)


# tree.inorden()

# # * tree.replace("Mario", "Pareraaa", "city")

# buscado = input("Ingrese un nombre: ")

# resultado = tree.nearby_search(buscado, "name")
# print("\nResultado de la busqueda: ")
# for item in resultado:
#     print(item)

#tree.inorden()

my_dict = {"nombre":"Curtis", "ciudad":"Urdinarrain", "edad":21}

print(my_dict.get("nombre") == "Curtis")