from list import barrido_dict, remove, barrido, search, show, search_to_list, FilterByLetter, FrequencyCounter
from random import randint, shuffle
import operator

lista_heroes = [
    {
        "name" : "Spider-Man",
        "real_name" : "Peter Parker",
        "ano_aparicion" : 1962,
        "casa_comic" : "Marvel",
        "biografia" : 'Peter Parker, un estudiante de secundaria, fue mordido por una araña radioactiva, lo que le otorgó habilidades sobrehumanas, como fuerza, agilidad y la capacidad de trepar paredes. Después de la trágica muerte de su tío Ben, Peter adopta el mantra de "Con gran poder, viene una gran responsabilidad" y lucha contra el crimen como Spider-Man.'
    },
    {
        "name" : "Iron Man",
        "real_name" : "Tony Stark",
        "ano_aparicion" : 1963,
        "casa_comic" : "Marvel",
        "biografia" : 'Tony Stark, un genio multimillonario, industrial y filántropo, construyó una armadura avanzada para salvar su vida después de ser herido y capturado por terroristas. Utiliza su intelecto y recursos para proteger al mundo como Iron Man, enfrentando amenazas tanto tecnológicas como sobrenaturales.'
    },
    {
        "name" : "Captain America",
        "real_name" : "Steve Rogers",
        "ano_aparicion" : 1941,
        "casa_comic" : "Marvel",
        "biografia" : 'Durante la Segunda Guerra Mundial, Steve Rogers se ofreció como voluntario para un experimento del gobierno estadounidense que lo transformó en el súper soldado conocido como Captain America. Con su escudo indestructible y su sentido del deber, lucha por la libertad y la justicia.'
    },
    {
        "name" : "Wolverine",
        "real_name" : "James 'Logan' Howlett",
        "ano_aparicion" : 1974,
        "casa_comic" : "Marvel",
        "biografia" : 'Logan, también conocido como Wolverine, es un mutante con habilidades regenerativas, sentidos agudizados y garras retráctiles de adamantium. Es miembro de los X-Men y ha sido parte de numerosos equipos, enfrentando tanto a enemigos humanos como mutantes.'
    },
    {
        "name" : "Black Panter",
        "real_name" : "T'Challa",
        "ano_aparicion" : 1966,
        "casa_comic" : "Marvel",
        "biografia" : "T'Challa es el rey de Wakanda, una nación africana tecnológicamente avanzada. Como el Black Panther, posee habilidades sobrehumanas y utiliza un traje hecho de vibranium. Lucha por proteger su reino y el mundo, combinando sus deberes como rey y superhéroe."
    },
    {
        "name" : "Superman",
        "real_name" : "Clark Kent (Kal-El)",
        "ano_aparicion" : 1938,
        "casa_comic" : "DC Comics",
        "biografia" : "Nacido en el planeta Krypton como Kal-El, fue enviado a la Tierra antes de la destrucción de su planeta. Adoptado por una familia humana, creció como Clark Kent. Con poderes sobrehumanos bajo el sol amarillo de la Tierra, lucha por la verdad y la justicia como Superman."
    },
    {
        "name" : "Batman",
        "real_name" : "Bruce Wayne",
        "ano_aparicion" : 1939,
        "casa_comic" : "DC Comics",
        "biografia" : "Bruce Wayne, un multimillonario huérfano, juró vengar la muerte de sus padres combatiendo el crimen en Gotham City. Sin superpoderes, utiliza su intelecto, habilidades de combate y tecnología avanzada para luchar contra villanos como el Joker y Two-Face."
    },
    {
        "name" : "Wonder Woman",
        "real_name" : "Diana Prince",
        "ano_aparicion" : 1941,
        "casa_comic" : "DC Comics",
        "biografia" : "Diana, princesa de las Amazonas, es una guerrera entrenada desde su infancia en la isla de Themyscira. Con poderes otorgados por los dioses griegos, lucha por la paz y la justicia en el mundo humano como Wonder Woman, usando su lazo de la verdad, brazaletes indestructibles y su tiara."
    },
    {
        "name" : "Flash",
        "real_name" : "Barry Allen",
        "ano_aparicion" : 1956,
        "casa_comic" : "DC Comics",
        "biografia" : "Barry Allen, un científico forense, obtuvo su supervelocidad tras un accidente en su laboratorio. Como The Flash, protege Central City y el multiverso de amenazas con su capacidad de moverse a velocidades increíbles."
    },
    {
        "name" : "Aquaman",
        "real_name" : "Arthur Curry",
        "ano_aparicion" : 1941,
        "casa_comic" : "DC Comics",
        "biografia" : "Arthur Curry es el rey de Atlantis y protector de los océanos. Con la capacidad de comunicarse con la vida marina, fuerza sobrehumana y la habilidad de respirar bajo el agua, lucha por mantener el equilibrio entre el mundo de la superficie y el mar."
    },
    {
        "name" : "Green Lantern",
        "real_name" : "Hal Jordan",
        "ano_aparicion" : 1959,
        "casa_comic" : "DC Comics",
        "biografia" : "Hal Jordan es un piloto de pruebas que recibe un anillo de poder de un extraterrestre moribundo, convirtiéndose en miembro de los Green Lantern Corps, una fuerza policial intergaláctica. El anillo le otorga la capacidad de crear cualquier cosa que imagine, usando su voluntad como fuente de poder."
    },
    {
        "name" : "Dr. Strange",
        "real_name" : "Stephen Strange",
        "ano_aparicion" : 1963,
        "casa_comic" : "DC Comics",
        "biografia" : "Stephen Strange, un renombrado neurocirujano, sufrió un accidente de coche que dañó sus manos, impidiéndole continuar con su carrera. En busca de una cura, viajó al Tíbet y encontró al Anciano, un místico que le enseñó las artes místicas. Stephen se convirtió en el Hechicero Supremo, protegiendo la Tierra contra amenazas mágicas y sobrenaturales. Con la ayuda de su capa de levitación, el Ojo de Agamotto y un vasto conocimiento de la magia, Doctor Strange defiende el universo de fuerzas oscuras y multidimensionales."
    },
    {
        "name" : "Captain Marvel",
        "real_name" : "Carol Danvers",
        "ano_aparicion" : 1968,
        "casa_comic" : "Marvel",
        "biografia" : "Carol Danvers, una piloto de la Fuerza Aérea de los Estados Unidos, adquirió habilidades sobrehumanas después de un accidente que involucró tecnología extraterrestre de los Kree. Originalmente conocida como Ms. Marvel, Carol adoptó el título de Captain Marvel en honor a su mentor, el guerrero Kree Mar-Vell. Como Captain Marvel, posee una fuerza y resistencia sobrehumanas, la capacidad de volar y la habilidad de proyectar y absorber energía. Carol lucha para proteger la Tierra y el universo, enfrentándose a amenazas cósmicas y sirviendo como un símbolo de poder y determinación. Su historia refleja su crecimiento desde una oficial militar hasta una de las heroínas más poderosas del universo Marvel."
    },
    {
        "name" : "Star Lord",
        "real_name" : "Peter Guill",
        "ano_aparicion" : 1976,
        "casa_comic" : "Marvel",
        "biografia" : "Peter Quill, conocido como Star-Lord, es el hijo de una mujer humana y el rey extraterrestre J'son de Spartax. Abducido por un grupo de piratas espaciales liderados por Yondu después de la muerte de su madre, Peter creció en el espacio y eventualmente se convirtió en un aventurero y ladrón. Equipado con una variedad de armas avanzadas y su casco característico, Star-Lord es un maestro estratega y combatiente. Es el líder de los Guardianes de la Galaxia, un grupo de héroes intergalácticos que protegen el cosmos de amenazas como Ronan el Acusador y Thanos. Con su actitud desenfadada y sentido del humor, Peter Quill se destaca como un héroe atípico que lucha por el bien del universo."
    }
    
]

def mostrar_ocurrencia(lyst : list, key : str, *args):
    for index, element in enumerate(lyst):
        for ocurrence in args:
            if ocurrence in element[key]:
                print(f"# {ocurrence=}:")
                show(lyst, index, "name", "real_name")
                
def mostar_ano_aparicion(lyst : list):
    for index, element in enumerate(lyst):
        if (element['ano_aparicion'] < 1963):
            show(lyst, index, "name", "real_name")




shuffle(lista_heroes)

# barrido_dict(lista_heroes)
    
# todo: Eliminar el nodo que tiene la informacion de Linterna Verde (Green Lantern)

remove(lista_heroes, "name", "Green Lantern")

barrido(lista_heroes, "name", "real_name")

# todo: mostrar el anio de aparición de Wolveriine
position = search(lista_heroes, "name", "Wolverine")
if (position is not None):
    print(f"El anio de aparicion de Wolverine es: {lista_heroes[position]['ano_aparicion']}")
else:
    print(f"El Heroe que busco no existe en la lista.")

# todo: cambiar la casa de Dr. Strange a Marvel

print()
position = search(lista_heroes, "name", "Dr. Strange")
if (position is not None):
    print(">Before")
    show(lista_heroes, position, "name", "real_name", "ano_aparicion", "casa_comic")
    lista_heroes[position]['casa_comic'] = "Marvel"
    print(">After")
    show(lista_heroes, position, "name", "real_name", "ano_aparicion", "casa_comic")
else:
    print(f"No existe el heroe.")

# todo: mostrar el nombre de aquellos superheroes que en su biografia menciona la palabra "traje" o "armadura"

mostrar_ocurrencia(lista_heroes, "biografia", "traje", "armadura")

# todo: mostrar el nombre y la casa de los superheroes cuya fecha de aparicion sea anterior a 1963

# ! METODO 1
print("METODO 1:")
for item in list(filter(lambda x : x['ano_aparicion'] < 1963, lista_heroes)):
    print(
        f"'name' : {item['name']} -",
        f"'real_name' : {item['real_name']} -",
        f"'ano_aparicion' : {item['ano_aparicion']}"
    )

# ! METODO 2
print("\nMETODO 2:")
mostar_ano_aparicion(lista_heroes)

# todo: mostrar la casa a la que pertenece Capitana Marvel (Captain Marvel) y Mujer Maravilla (Wonder Woman);

print("Casa en las que aparecen: ")

lista_buscado = search_to_list(lista_heroes, "name", "Captain Marvel", "Wonder Woman")

barrido(lista_buscado, "name", "casa_comic")

# todo: mostrar toda la informacion de Flash y Star-Lord

print("Toda la informacion de: ")

lista_buscado = search_to_list(lista_heroes, "name", "Flash", "Star Lord")

barrido(lista_buscado)

# todo: listar los superhéroes que comienzan con la letra B, M y S

print("Superheroes que empiezan con la letra B, M y S: ")

lista_filtrado = FilterByLetter(lista_heroes, "name", "B", "M", "S")

barrido(lista_filtrado, "name", "real_name")

# todo: determinar cuantos superheroes hay de cada casa de comic

print("Cantidad de superheroes por casa de comic: ")

lista_contado = FrequencyCounter(lista_heroes, "casa_comic", "Marvel", "DC Comics")

for casa in lista_contado:
    print(f"Casa de Comic: '{casa[1]}', Cantidad de Heroes: '{casa[0]}'.")

