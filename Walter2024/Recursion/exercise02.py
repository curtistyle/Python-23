def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero - 1)
    
NUMERO = 4
print(f"La suma comprendida entre 0 y {NUMERO} es: {sumatoria(NUMERO)}")

