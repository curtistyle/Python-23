valores = [
    {'aristas': [{'value':"A"},{'value':"B"},{'value':'C'}]},
    {'aristas':[{'value':"B"}]},
    {'aristas':[{'value':"B"}, {'value':"C"}]},
    {'aristas':[{'value':"B"}]}
]



contador = {}

for item in valores:
    for arista in item['aristas']:
        if not arista['value'] in contador.keys():
            contador.update({arista['value']:1})
        else:
            contador[arista['value']] += 1


print(contador)

temp = {"lunes":1,"martes":2}

for item in temp:
    print(item)
    
    
class Persona:
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age
    
    def __eq__(self, value: object) -> bool:
        return self.name == value.name
    
persona1 = Persona("Carlo", 12)
persona2 = Persona("Carlos", 22)



print(persona1==persona2)


asd = set()

