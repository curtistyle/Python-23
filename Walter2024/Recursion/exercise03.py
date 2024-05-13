def producto(x, y):
    if y == 0:
        return 0
    else:
        return x + producto(x, y - 1)

numero1, numero2 = 5, 5

print(f"El producto de {numero1} y {numero2} es: {producto(numero1, numero2)}")