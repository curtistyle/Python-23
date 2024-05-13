def toBinary(numero):
    if numero == 0:
        return ''
    else:
        return  toBinary(numero // 2) + str(numero % 2)
    

NUMERO = 2

print(f"El numero {NUMERO} se representa en binario como {toBinary(NUMERO)}.")