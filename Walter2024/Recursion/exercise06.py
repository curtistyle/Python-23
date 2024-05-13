def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ''
    else:
        return cadena[-1] + invertir_cadena(cadena[0:len(cadena) - 1])
    
print(invertir_cadena("Welcome to my Console App!"))