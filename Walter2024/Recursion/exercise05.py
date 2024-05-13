def romano_a_decimal(letra):
    if letra == "I":
        return 1
    elif letra == "V":
        return 5
    elif letra == "X":
        return 10
    elif letra == "L":
        return 50
    elif letra == "C":
        return 100
    elif letra == "D":
        return 500
    else:
        return 0

def conversion(romano):
    if len(romano) <= 1:
        return romano_a_decimal(romano)
    else:
        numero_actual = romano_a_decimal(romano[0])
        numero_siguiente = romano_a_decimal(romano[1])
        
        if numero_actual >= numero_siguiente:
            return numero_actual + conversion(romano[1:len(romano)])
        else:
            return conversion(romano[1:len(romano)]) - numero_actual

NUMERO_ROMANO = "CCVL"

print(f"El numero romano {NUMERO_ROMANO} es en decimal: {conversion(NUMERO_ROMANO)}")

