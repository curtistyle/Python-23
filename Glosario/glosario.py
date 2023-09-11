class Glosario:
    
    def __init__(self, glosario_list={}):
        self.glosario_list = glosario_list
        
    @property
    def Glosario_List(self):
        return self.glosario_list
    
    @Glosario_List.setter
    def Glosario_List(self, value):
        self.glosario_list = value
    
    def update_glosario(self, value, key):
        if isinstance(key, str):
            newglosario = {key : value}
            self.glosario_list.update(newglosario)
        else:
            raise ValueError("The key of dicctionary must be a str type.")
    
if __name__ == '__main__':
    glo = Glosario()
    
    try:
        glo.update_glosario('Palabra', 2)
        print(glo.Glosario_List) 
    except ValueError as e:
        print("Error! ",e)
    
    