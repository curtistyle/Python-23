lista = [1, 2, 3, 4, 5]

print(lista)

print(f" > tamanio: {len(lista)}")

print(f" > mitad - pos:{len(lista)//2} item:{lista[len(lista)//2]}")

print(f" > izquierda: {lista[:len(lista)//2]}")

print(f" > derecha: {lista[len(lista)//2+1:]}")




filas = len(tbl)
columnas = len(tbl[0])

print(f"FILAS: {filas}")
print(f"COLUMNAS: {columnas}")

print("x ", tbl[0])


def limite(lst:list, x:int, y:int) -> bool:
    return True if (x < len(lst)) and (y < len(lst[0])) else False


print("Limtie_:", limite(tbl, 9, 10))

tbl = [
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,0,1,0,1,0,1,0],
    [0,1,0,0,1,0,1,0,1,0],
    [0,1,0,1,1,0,1,0,1,1],
    [1,1,0,1,0,0,1,0,0,1],
    [0,0,0,1,0,1,0,0,1,0],
    [0,1,1,1,0,0,1,0,1,0],
    [0,1,0,0,1,0,1,0,1,0],
    [0,1,1,0,1,0,1,0,1,0],
    [0,0,0,0,1,0,0,0,1,2],
    ]

def laberinto(tablero:list, x, y):
    # a, b : partida del tablero & ultima opcion
    if (tablero[x][y] == 2):
        return "Llegaste"
    elif (tablero[x][y] == 0):
        tablero[x][y] = 3
        # abajo
        if (limite(tablero, x+1, y)) and (tablero[x+1][y] == 0):
            return laberinto(laberinto,x+1,y)
        #derecha
        elif (limite(tablero, x+1, y+1)):
            



