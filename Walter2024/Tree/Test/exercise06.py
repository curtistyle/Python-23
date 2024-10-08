"""Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos 
tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las 
siguientes consignas: """

"""
    a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
    b. realizar un barrido inorden del árbol por nombre y ranking;
    c. realizar un barrido por nivel de los árboles por ranking y especie;
    d. mostrar toda la información de Yoda y Luke Skywalker;
    e. mostrar todos los Jedi con ranking “Jedi Master”;
    f. listar todos los Jedi que utilizaron sabe de luz color verde;
    g. listar todos los Jedi cuyos maestros están en el archivo;
    h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
    i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
    """


jedis = [
    {"nombre": "Luke Skywalker", "especie": "Humano", "ano_nacimiento": "19 BBY", "color_sable": "Azul", "Ranking": "Jedi Knight", "maestro": "Yoda"},
    {"nombre": "Yoda", "especie": "Yoda", "ano_nacimiento": "896 ABY", "color_sable": "Verde", "Ranking": "Jedi Grand Master", "maestro": "N/A"},
    {"nombre": "Obi-Wan Kenobi", "especie": "Humano", "ano_nacimiento": "57 BBY", "color_sable": "Azul", "Ranking": "Jedi Master", "maestro": "Qui-Gon Jinn"},
    {"nombre": "Qui-Gon Jinn", "especie": "Humano", "ano_nacimiento": "92 BBY", "color_sable": "Verde", "Ranking": "Jedi Master", "maestro": "Count Dooku (antes de volverse Sith)"},
    {"nombre": "Mace Windu", "especie": "Humano", "ano_nacimiento": "72 BBY", "color_sable": "Violeta", "Ranking": "Jedi Master", "maestro": "Desconocido"},
    {"nombre": "Anakin Skywalker / Darth Vader", "especie": "Humano", "ano_nacimiento": "41.9 BBY", "color_sable": "Azul (antes), Rojo (después)", "Ranking": "Jedi Knight (antes), Sith Lord (después)", "maestro": "Obi-Wan Kenobi"},
    {"nombre": "Rey", "especie": "Humana", "ano_nacimiento": "Desconocido", "color_sable": "Azul", "Ranking": "Jedi Knight", "maestro": "Luke Skywalker"},
    {"nombre": "Ahsoka Tano", "especie": "Togruta", "ano_nacimiento": "36 BBY", "color_sable": "Blanco", "Ranking": "Jedi Knight", "maestro": "Anakin Skywalker"},
    {"nombre": "Kanan Jarrus", "especie": "Humano", "ano_nacimiento": "Desconocido", "color_sable": "Azul", "Ranking": "Jedi Knight", "maestro": "Desconocido (aprendió por sí mismo)"},
    {"nombre": "Ezra Bridger", "especie": "Humano", "ano_nacimiento": "Desconocido", "color_sable": "Azul", "Ranking": "Padawan", "maestro": "Kanan Jarrus"}
]



