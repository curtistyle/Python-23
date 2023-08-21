import json

person = {
    "name" : "Juan",
    "age"  : 21,
    "city" : "Buenos Aires"
}


json_string = json.dumps(person)

person = json.loads(json_string)

print(person["name"])