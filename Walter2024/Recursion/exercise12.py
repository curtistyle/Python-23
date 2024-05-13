def mcd(x, y):
    if y == 0:
        return x    
    else:
        return mcd(y, x % y)


NUM1 = 252
NUM2 = 105

print(f"{mcd(NUM1, NUM2)} es el \'Maximo Comun Divisor\' de {NUM1} y {NUM2}.")
