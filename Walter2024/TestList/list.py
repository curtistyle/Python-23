class MyList(list):
    def __init__(self,*args):
        super().__init__(*args)
        
    def showForKeys(self, *keys):
        if self == []:
            return None
        if keys != ():
            for item in self:
                for index, key in enumerate(keys):
                    print(f"'{key}' = {item[key]}, ", end="") if (index < (len(keys) - 1)) else print(f"'{key}' = {item[key]}. ", end="")
                print()
    
    def getNode(self, index):
        if index >= 0 and index < len(self):
            return self[index]
        else:
            raise ValueError("index list out of range")
    
    def getSubList(self, index, key):
        if (type(self[index][key]) == type(list())):
            return MyList(self[index][key])
        else:
            raise ValueError(f"the {key} is not list type")
        
    def search(self, key, value):
        for index, item in enumerate(self):
            if item[key] == value:
                return index
        else:
            return -1

    def maxForKey(self, key):
        """returns the `index` of the maximum `item` of the `list`"""
        return max(enumerate(self), key=lambda value : value[1][key])[0]