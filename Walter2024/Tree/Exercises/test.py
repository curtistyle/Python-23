class Person:
    def __init__(self, name, age, country) -> None:
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age}, {self.country})"




# person = Person("Curtis", 22, "Urdinarrain")

# print(person)

person = {"name" : "curtis", "city" : "Urdinarrain", "age" : 12}




