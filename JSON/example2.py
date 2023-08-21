import json

person = {
    "name":"Carlos",
    "age" : 22,
    "city":"Bs As"
}


# Escribir en un archivo
with open("datos.json", "w") as archivo:
    json.dump(person,archivo)
    
    


