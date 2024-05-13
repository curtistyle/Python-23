def sumardigitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + sumardigitos(numero // 10)
    

NUMERO = 1234

print(f"La suma de los digitos del numero: \'{NUMERO}\' da como resultado: {sumardigitos(NUMERO)}.")

