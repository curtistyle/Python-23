def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
    
    
NUMERO = 8
print(f"El Fibonacci de {NUMERO} es {fibonacci(NUMERO)}.")


