def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)


NUMERO = 123

print(f"El numero {NUMERO} tiene n={contar_digitos(NUMERO)} digitos.")

