import json
from os import remove,close

def crear_archivo(name : str, extension='.json'):
    name = name + extension 
    """ (w) abierto para escritura"""
    fichero = open(name, 'w', errors='namereplace')
    fichero.close()
    return fichero, name

def abrir_archivo(name : str):
    """ (r) abierto para lectura"""
    fichero = open(name,'r')
    return fichero
    

def borrar_archivo(name : str):
    try:
        abrir_archivo(name)
        remove(name)
        print("El fichero fue borrado.")
    except FileNotFoundError:
        print("El fichero no existe.")
        
    

    

    # if open(name, 'r') is FileNotFoundError:
    #     f = open(name,'w')
    # else:
    #     print("El archivo existe papu")
    # return f


if __name__=='__main__':
    #abrir_archivo('ASD.json')
    
    
    borrar_archivo('banda.json')
    
    