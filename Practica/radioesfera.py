import math

radio = float(input('Ingrese el radio de una Esfera: '))

diametro = 2.0 * radio

circunferencia = float(math.pi) * diametro  # math.pi devuelve el numero pi 

area_superdicie = 4 * math.pi * radio**2

volumen = 4/3 * math.pi * radio**3

print('Diametro: ', "{:.2f}".format(diametro), 
    '\nCircunferencia: ', "{:.2f}".format(circunferencia), 
    '\nArea de la superficie: ', "{:.2f}".format(area_superdicie), 
    '\nVolumen: ', "{:.2f}".format(volumen))



