from stack import Stack

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

]

# ? Implementaciones

def buscar_en_la_pila(pila : Stack, buscado, key) -> bool:
    pila_temp = Stack()
    encontrado = False
    
    while not (pila.is_empty()):
        elemento = pila.pop()
        if elemento[key] == buscado[key]:
            encontrado = True
        pila_temp.push(elemento)
    
    while not (pila_temp.is_empty()):
        pila.push(pila_temp.pop())
    
    return encontrado

def mostrar_tabla(values):
    for key, item in values.items():
        print(f"'{key}' : {item}")
        
def barrido(pila : Stack, *args):
    pila_temp = Stack()

    while not (pila.is_empty()):
        pila_temp.push(pila.pop())
    
    while not (pila_temp.is_empty()):
        if args != ():
            for key in args:
                print(f"'{key}' : {pila_temp.top()[key]}")
        else:
            print(pila_temp.top())
            
        pila.push(pila_temp.pop())


# todo: Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

# * Apilar la lista en la pila

pila_dinosaurios = Stack()

for dinosaurio in dinosaurios:
    pila_dinosaurios.push(dinosaurio)
    
# todo: (a) contar cuantas especies hay

pila_temp = Stack()
tabla_especie = {}

while not (pila_dinosaurios.is_empty()):
    dinosaurio = pila_dinosaurios.pop()
    if (dinosaurio["especie"] not in tabla_especie):
        tabla_especie[dinosaurio["especie"]] = 0
    tabla_especie[dinosaurio["especie"]] += 1
    
    pila_temp.push(dinosaurio)

while not (pila_temp.is_empty()):
    pila_dinosaurios.push(pila_temp.pop())
    
print(f"(a) El total de dinosaurios son {pila_dinosaurios.size()} y su cantidad por especie es: ")
mostrar_tabla(tabla_especie)
        

# todo: (b) determinar cuantos descubridores distintos hay

pila_descubridores = Stack()
pila_temp = Stack()

while not (pila_dinosaurios.is_empty()):
    buscado = pila_dinosaurios.top()
    if not (buscar_en_la_pila(pila_descubridores, buscado, "especie")):
        pila_descubridores.push(buscado)
    pila_temp.push(pila_dinosaurios.pop())

while not (pila_temp.is_empty()):
    pila_dinosaurios.push(pila_temp.pop())
    
print(f"\n(b) Hay {pila_descubridores.size()} distintos: ")
barrido(pila_descubridores, "descubridor")

# todo: (c) Mostrar todos los dinosaurios que empiecen con T
pila_temp = Stack()

print("\n(c) Dinosaurios que empiezan con la letra T: ")

while not (pila_dinosaurios.is_empty()):
    dinosaurio = pila_dinosaurios.pop()
    if dinosaurio['nombre'].startswith('T'):
        print(dinosaurio['nombre'])
    pila_temp.push(dinosaurio)
    
while not (pila_temp.is_empty()):
    pila_dinosaurios.push(pila_temp.pop())
    
# todo: Mostrar todos los dinosaurio que pesen menos de 275 Kg 
pila_temp = Stack()

print("\n(d) Dinosaurios que pesan menos de 275 kg: ")

print(f'{"Nombre":<20}{"Peso":>12}')
while not (pila_dinosaurios.is_empty()):
    dinosaurio = pila_dinosaurios.pop()
    if int(dinosaurio['peso'].split(" ")[0]) < 275:
        print(f"{dinosaurio['nombre']:<20}{dinosaurio['peso']:>12}")
    pila_temp.push(dinosaurio)
    
while not (pila_temp.is_empty()):
    pila_dinosaurios.push(pila_temp.pop())
    
# todo: (e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S

pila_temp = Stack()
nueva_pila = Stack()

while not (pila_dinosaurios.is_empty()):
    dinosaurio = pila_dinosaurios.pop()
    if (dinosaurio['nombre'].startswith(("A", "Q", "S"))):
        nueva_pila.push(dinosaurio)
    else:
        pila_temp.push(dinosaurio)

while not (pila_temp.is_empty()):
    pila_dinosaurios.push(pila_temp.pop())    
    
print("\n(e) Pila con los dinosaurios que empiezan con la letra A, Q y S: ")
barrido(nueva_pila)