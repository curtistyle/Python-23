def logaritmo(exponente, base):
    if exponente <= base:
        return 1
    else:
        return 1 + logaritmo(exponente // base, base)

EXPONENTE = 1000
BASE = 10

print(f"El logaritmo de {EXPONENTE} con base {BASE} es: ", logaritmo(EXPONENTE, BASE))