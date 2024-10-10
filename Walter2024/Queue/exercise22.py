""" Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino 
F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades: """

from cola import Queue


class Personaje:
    def __init__(self, nombre, heroe, genero) -> None:
        self.nombre=nombre
        self.heroe=heroe
        self.genero=genero
        
    def obtener_genero_normalizado(self):
        return "Masculino" if (self.genero == "M") else "Femenino"
    
    def __str__(self) -> str:
        return f"{__class__.__name__}({self.nombre}, {self.heroe}, {self.genero})"
    
    def __repr__(self) -> str:
        return f"\'{self.nombre}\' es el heroe \'{self.heroe}\' y su genero es \'{self.obtener_genero_normalizado()}\'."


# * mostrar elementos de una cola

def barrido(cola : Queue):
    for indice in range(cola.size()):
        print(cola.on_front())
        cola.move_to_end()
    

mcu = Queue()

lista_personajes = [
    Personaje("Tony Stark", "Iron Man", "M"),
    Personaje("Steve Rogers", "Capitán América", "M"),   
    Personaje("Natasha Romanoff", "Black Widow", "F"),   
    Personaje("Thor Odinson", "Thor", "M"),   
    Personaje("Bruce Banner", "Hulk", "M"),   
    Personaje("Carol Danvers", "Capitana Marvel", "F"),   
    Personaje("Peter Parker", "Spider-Man", "M"),   
    Personaje("T'Challa", "Black Panther", "M"),  
    Personaje("Wanda Maximoff", "Scarlet Witch", "F"),  
    Personaje("Stephen Strange", "Doctor Strange", "M"),
    Personaje("Scott Lang","Ant-Man","M")
]

for personaje in lista_personajes:
    mcu.arrive(personaje)

# todo: a. determinar el nombre del personaje de la superhéroe Capitana Marvel;

print("\n(a) Determina el nombre del persoaje de la superheroe Capitana Marvel\n")

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if (personaje.heroe == "Capitana Marvel"):
        print(personaje.nombre)
        
    mcu.move_to_end()


# todo: b. mostrar los nombre de los superhéroes femeninos;

print("\n(b) Personajes MCU Femeninos.\n")

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if (personaje.genero == "F"):
        print(repr(personaje))
        
    mcu.move_to_end()
    
    
# todo: c. mostrar los nombre de los superhéroes Masculino;

print("\n(c) Personajes MCU Masculinos.\n")

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if (personaje.genero == "M"):
        print(repr(personaje))
        
    mcu.move_to_end()

# todo: d. determinar el nombre del superhéroe del personaje Scott Lang;

print("\n(d) Determina el nombre del superheroe del personaje Scott Lang.\n")

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if (personaje.nombre == "Scott Lang"):
        print(personaje.heroe)
        
    mcu.move_to_end()
    
# todo: e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;

print("\n(e) Mostrar todos los datos de los superheroes o persoajes cuyos nombre comienzan con la letra \'S\'")

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if ((personaje.nombre.startswith("S")) or (personaje.heroe.startswith("S"))):
        print(repr(personaje))
        
    mcu.move_to_end()

# todo: f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

print("\n(e) Mostrar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes")

buscado = "Carol Danvers"

encontrado = False

for indice in range(mcu.size()):
    personaje : Personaje = mcu.on_front()
    
    if (personaje.nombre == buscado):
        encontrado = True
        print(repr(personaje))
        
    mcu.move_to_end()
    
if not (encontrado):
    print(f"{buscado} no esta en la cola")