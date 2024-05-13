def susecion(numero):
    if numero == 1:
        return 1
    else:
        return 1 / numero + susecion(numero - 1)
    
NUMERO = 4
print(f"La susesion 1 + ... 1/{NUMERO} da como resultado: {susecion(NUMERO)}")
