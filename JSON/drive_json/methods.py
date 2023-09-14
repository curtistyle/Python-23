import json

def crear_archivo(name : str):
    name = name + '.json'
    try: 
        open(name, 'x')
    except FileExistsError:
        print("El archivo ya existe")
    
    # if open(name, 'r') is FileNotFoundError:
    #     f = open(name,'w')
    # else:
    #     print("El archivo existe papu")
    # return f

def abrir_archivo(name :str):
    pass

if __name__=='__main__':
    crear_archivo("banda")
    
    