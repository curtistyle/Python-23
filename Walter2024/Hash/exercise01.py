from random import randint, choice

# ? (a) Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen anterior contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;

from random import randint, choice


def hash_legion(value):
    return trooper[:2]

def hash_numerica(value):
    return trooper[-3:]


legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

table_legiones = {}
table_numerica = {}

for legion in legiones:
    table_legiones[legion] = []

for i in range(0, 2000):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    clave = hash_numerica(trooper)
    if clave not in table_numerica:
        table_numerica[clave] = []

    # TODO: deberá cargar los Stormtrooper generados en dos tablas hash encadenadas, en la primera se deberá agrupar de acuerdo a los tres últimos dígitos del código y en la segunda a partir de las iniciales de la legión.

    # * ej: 967 - ['FL-4967', 'FO-5967']
    # ? Tabla que esta agrupada de acuerdo a los tres ultimos dígitos del codigo
    table_numerica[clave].append(trooper)
    
    # * ej: FO - ['FO-8126', 'FO-9917', 'FO-3593']
    # ? Tabla que esta agrupada de acuerdo a las iniciales de la legión
    table_legiones[hash_legion(trooper)].append(trooper)
    
# for key, item in table_numerica.items():
#     print(f"{key} - {item}")
    
# for key, item in table_legiones.items():
#     print(f"{key} - {item}")


# TODO: determinar si el Stormtrooper FN-2187 está cargado para poder quitarlo porque es un traidor desertor.

# if "FN-2187" == table_legiones.get("FN"):
    

list_187 = table_numerica.get('187', [])
if 'FN-2187' in list_187:
    pos_fn_2187 = list_187.index('FN-2187')
    if pos_fn_2187 > -1:
        print(f'esta en la posicion {pos_fn_2187}')
else:
    print('no esta')
print(len(list_187))
print()