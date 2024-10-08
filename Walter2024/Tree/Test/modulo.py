def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por 0")
    return x / y

def multiplicar(x, y):
    return x * y

operaciones = [
    sumar,
    restar,
    dividir,
    multiplicar
]

for operacion in operaciones:
    print(operacion(2,2), operacion.__name__)
    

times = [
    {"day":"Lunes", "time_current" : 1},
    {"day":"Martes", "time_current" : 12},
    {"day":"Domingo", "time_current" : 1234567},
    {"day":"Jeves", "time_current" : 1234},
]



def modicar(obj : dict):
    for key, value in obj.items():
        print(f"{key} - {value}")
        

modicar(times[0])