import json

persons = [
    {"name": "J. Garcia", "number": 13, "holder": True},
    {"name": "L. Blondel", "number": 42, "holder": True},
    {"name": "J. Figal", "number": 4, "holder": True},
    {"name": "M. Sarachi", "number": 3, "holder": True},
    {"name": "C. Medina", "number": 36, "holder": True},
    {"name": "J. Campuzano", "number": 49, "holder": True},
    {"name": "E. Fernandez", "number": 21, "holder": True},
    {"name": "E. Zeballos", "number": 7, "holder": True},
    {"name": "E. Cavani", "number": 10, "holder": True},
    {"name": "L. Jason", "number": 11, "holder": True}    
]

for person in persons:
    print(person['name'])