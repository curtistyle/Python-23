import json

# leer un archivo

with open("datos.jsoin", "r") as archivo:
    data = json.load(archivo)
    print(data)
    
    json.dump