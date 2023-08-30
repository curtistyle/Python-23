class Tiempo:
    
    def __init__(self,h=0,m=0,s=0):
        self.__hora = h
        self.__minuto = m
        self.__segundo = s
    
    def __str__(self):
        return f'{self.__hora=} {self.__minuto=} {self.__segundo=}'
    
    @property
    def Hora(self):
        return self.__hora
           
    @Hora.setter
    def Hora(self, value):
            if not ((value >= 0) and (value <= 24)):
                raise ValueError("Rango de seteo invalido.")
            else:
                self.__hora = value
                 
tiempo1 = Tiempo()
 
tiempo1.Hora = 20  
        