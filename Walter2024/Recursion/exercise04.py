def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
BASE = 10
EXPONENTE = 4    
    
print(f"{BASE} elevado a la {EXPONENTE} da como resultado: {potencia(BASE, EXPONENTE)}")

