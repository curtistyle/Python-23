import json
from os import remove,close

def crear_archivo(name : str, extension='.json'):
    name = name + extension 
    """ (w) abierto para escritura"""
    fichero = open(name, 'w', errors='namereplace')
    fichero.close()
    return name

def abrir_archivo(name : str):
    """ (r) abierto para lectura"""
    fichero = open(name,'r')
    return fichero
    
def escribir_archivo(name : str):
    """ (a) abierto para escritura """
    fichero = open(name, 'a')
    return fichero


def borrar_archivo(name : str):
    try:
        abrir_archivo(name)
        remove(name)
        print("El fichero fue borrado.")
    except FileNotFoundError:
        print("El fichero no existe.")
    
def json_a_archivo(dictionary : dict, name : str):
    try:
        file = escribir_archivo(name)
    except FileExistsError:
        print("El archivo no existe")
        crear_archivo(name)
        file = escribir_archivo(name)
    with file as value:
        json.dump(dictionary,value)

def archivo_a_json(name : str):
    try:
        file = abrir_archivo(name)
        dictionary = json.load(file)
        return dictionary
    except FileNotFoundError:
        print("El archivo no existe")
        return {}



if __name__=='__main__':
    # abrir_archivo('ASD.json')
    # borrar_archivo('banda.json')
    
    """ ejemplo diccionario banda"""
    banda = {
        "banda" : [
            {
                "title"  : "The Offspring",
                "list"   : 1,
                "albums" : [
                    {
                        "title"      : "Americana",
                        "year"       : "1998",
                        "track_list" : [
                            {
                                "title"  : "Have You Ever",
                                "time"   : "03:50",
                                "number" : 2
                            },
                            {
                                "title"  : "Staring At The Sun",
                                "time"   : "02:13",
                                "number" : 3
                            }
                        ] 
                    },
                    {
                        "title"      : "Splinter",
                        "year"       : "2003",
                        "track_list" : [
                            {
                                "title"  : "Necon",
                                "time"   : "3:18",
                                "number" : 1
                            }
                        ]
                    }
                ]
            }
        ]

    }

    result = archivo_a_json('banda.json')
    print(result['banda'][0]['title'])
    
    # json_a_archivo(banda,'banda.json')
    
    