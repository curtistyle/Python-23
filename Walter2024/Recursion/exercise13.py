def mcd(x, y):
    if y == 0:
        return x    
    else:
        return mcd(y, x % y)

def mcm(a, b):
  if b == 0:
    return a
  else:
    return b * (a // mcd(a,b))


NUM1 = 12
NUM2 = 8

print(f"{mcm(NUM1, NUM2)} es el \'Minimo Comun Multiplo\' de {NUM1} y {NUM2}.")

