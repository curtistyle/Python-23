from exercise10 import contar_digitos

def invertir(numero):
    if numero < 10:
        return numero
    else:
        
        return (numero % 10) * 10 ** contar_digitos(numero // 10) + invertir(numero // 10)
    
NUMERO = 1123

print(f"El numero={NUMERO} invertido es: {invertir(NUMERO)}")