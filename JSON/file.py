import json

class File():
    dictionary_type = {"user" : None, "list" : []}
    
    def __init__(self, name) -> None:
        self.__path = name + ".json"
        self.__file = self.create()

            
    def create(self):
        try:
            return open(self.__path,'r')
        except FileNotFoundError:
            file = open(self.__path,'w')
            
            return file

    def add(self, **kwargs):
        dictionary = self.dictionary_type
        self.__file = open(self.__path, "a")
        for key, value in kwargs.items():
            dictionary.update({key : value})
        
        with self.__file as file:
            json.dump(dictionary,file)
        


if __name__ == "__main__":
    
    file = File("123123")
    
    file.add()
    
    