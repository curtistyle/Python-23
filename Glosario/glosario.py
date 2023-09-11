class Glosario:
    
    def __init__(self):
        self.__register = []
        self.__word = {} 
        
    @property
    def Word(self):
        """Return word atribute from Glosario object"""
        return self.__word
    
    @property
    def Register(self):
        """Return lists of dictionary glossaries from Glosario object"""
        return self.__register
        
    @Word.setter
    def Word(self, value):
        """Set word atribute from Glossary object"""
        self.__word = value
    
    @Register.setter
    def Register(self, value):
        """Set register atribute from Glossary object"""
        self.__register = value

    def __search(self, value, key="word"):
        """Searching `word` in register `list`, if value returns is not -1, return position of the `word`"""
        first = 0
        last = len(self.__register) - 1
        position = -1
        mid = (first + last + 1) // 2
        while ((position == -1) and (value <= self.__register[mid][key])):
            if (value == self.__register[mid][key]):
                position = mid
            elif (value < self.__register[mid][key]):
                last = mid - 1
            else:
                first = mid + 1
            mid = (first + last + 1) // 2
        return position 
     
    def add_word(self, value, key='word'):
        if isinstance(key, str):
            self.__word = {key : value}
            self.__register.append(self.__word)
        else:
            raise ValueError("The key of dicctionary must be a str type.")
        
    def delete_word(self, value, key='word'):
        pos = self.__search(value, key)
        print(">>> ", pos)
        if (pos != -1):
            self.__register.pop(pos)
        else:
            raise ValueError("The item searched is not exist.")
           
    def add_meaning(self, word, key, value : list):
        pos = self.__search(word)
        meaning = {key : value}
        return self.__register[pos].update(meaning)
    
    def delete_meaning(self):
        pass
    
        
if __name__ == '__main__':
    glo = Glosario()
    
    try:
        glo.add_word('How')
        glo.add_word('into')
        glo.add_word('store')
        glo.add_word('world')
    except ValueError as e:
        print("Error! ",e)
    
    print(glo.Register)
    glo.add_meaning('store','verb',['almacenar', 'guardar', 'conservar'])
    print(glo.Register)
    
    try:
        glo.delete_word('How')
        print(glo.Register)
    except ValueError as e:
        print("Error! ", e)
    
    
    