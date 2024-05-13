def usar_la_fuerza(mochila : list, sacar):
    if len(mochila) == 0:
        return [], -1
    elif mochila[len(mochila) - 1] == sacar:
        return mochila[len(mochila) - 1], len(mochila)
    else:
        mochila.pop()
        return usar_la_fuerza(mochila, sacar)

def usar_la_fuerza_2(mochila, sacar):
    if mochila == [] or mochila[-1] == sacar:
        return mochila
    else:
        return usar_la_fuerza_2(mochila[0:-1], sacar)
         


myList = [
    'Aerolupa', 
    'Artefato de la fuerza', 
    'Bastón de Landon Calrissian', 
    'Bola de cristal de Hermana de la Noche',
    'Brujula de Omega',
    'Brujua estelar Jedi',
    'Codex',
    'Cristal Nova',
    'Dados de Han Solo',
    'Esfera de la paz',
    'Guía del Contrabandista',
    'Infante de Shaa',
    'Joyas de la Corona de Alderaan',
    'Juego de Caligrafia de Ben Solo',
    'Los Archivos Rebeldes',
    'Reliquias',
    'Sable de Luz',
    'Soldado de Latón de Aux',
    "Um'Tal"
    ]

BUSCADO = "Sable de Luz"

print("### METODO 1:",end="\n\n")

objeto, ultimo = usar_la_fuerza(myList.copy(), BUSCADO)

if not(objeto == []):
    print(f"La mochila contiene el {objeto}.")
    print(f"Fueron necesario sacar \'{len(myList) - ultimo}\'")
else:
    print(f"La mochila no contiene el objeto buscado.")



print(f"\n### METODO 2:",end="\n\n")

total_objetos = len(myList)
ultimo = total_objetos - len(usar_la_fuerza_2(myList, BUSCADO))
print(f"** {total_objetos=}, {ultimo=} **")

if (ultimo < total_objetos):
    print(f"La mochila contiene el Sable de la Luz.")
else:
    print("El Sable de la Luz no se encuentra en la Mochila.")
    
print(f"Fueron necesario sacar \'{ultimo}\' objetos de la Mochila.")