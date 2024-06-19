class MyList(list):
    def __init__(self,*args):
        super().__init__(*args)
    
    def __is_dict(self):
        return type(self[0]) == type({})
    
    def __is_primitive(lyst):
        """
        Determina si los elementos de la lista son primitivos o no son TDA.
        
        Returns:
            `bool()` : `True` si los elementos son primitivos, de lo contrario `False`
        """
        return type(lyst[0]) in [type(str()), type(int()), type(float()), type(complex()), type(bool()), type(bytes()),type(bytearray()), type(str()), type(bytearray()), type(list())]
    
    def is_emty(self):
        """Determina si la lista esta vacia.

        Returns:
            `bool()`: retorna `True` si la lista esta Vacia.
        """
        return self == []
        
    def show(self):
        """
        Imprime los valores de cada elemento de la lista.        
        """
        for element in self:
            print(f"{str(element)}")
    
    def showForKeys(self, *keys : str) -> None:
        """
        Imprime los valores de las claves especificadas de cada elemento de la lista.
        Args:
            -`*keys`: Un número variable de argumentos de cadena que representan las claves para las que recuperar valores.
        """
        if self == []:
            return None
        if keys != ():
            if self.__is_dict():
                for item in self:
                    for index, key in enumerate(keys):
                        print(f"'{key}' = {item[key]}, ", end="") if (index < (len(keys) - 1)) else print(f"'{key}' = {item[key]}. ", end="")
                    print()
            else:
                for item in self:
                    for index, key in enumerate(keys):
                        print(f"'{key}' = {getattr(item, key)}, ", end="") if (index < (len(keys) - 1)) else print(f"'{key}' = {getattr(item, key)}. ", end="")
                    print()
        else:
            raise ValueError(f"{keys} is not defined.")
    
    def getNode(self, index : int):
        """
        Retorna el nodo de la lista de una determinada posicion.
        
        Args:
            -`index`: Posicion del nodo/item dentro de la lista.

        Returns:
            -`object`: El nodo en el índice especificado.
        """
        if index >= 0 and index < len(self):
            return self[index]
        else:
            raise ValueError("index list out of range")
    
    def getSubList(self, index, key):
        if (type(self[index][key]) == type(list())):
            return MyList(self[index][key])
        else:
            raise ValueError(f"the {key} is not list type")
     
    def __search_prim(self, value):
        for index, item in enumerate(self):
            if item == value:
                return index
        return -1
     
    def __search_dict(self, value, key):
        for index, item in enumerate(self):
            if item[key] == value:
                return index
        return -1
            
    def __search_obj(self, value, attr):
        for index, item in enumerate(self):
            if hasattr(item, attr) and (getattr(item, attr) == value):
                return index
        return -1
        
    def search(self, value, key=None) -> int:
        """
        Busca un elemento en la lista y devuelve la posicion de dicho elemento.
        
        Args: 
            -`value` (gerenic): Valor a comparar con los elementos de la lista.
            -`key`: La clave/atributo de cada `dict()` u `objeto` (TDA) que se ultizara para la comparacion. Si `key` no se define, la funcion va a iterar sobre datos primitivos `int()`, `str()` o `float()`
            
        Returns:
            -`int()`: Si el valor existe en la lista retorna la posición, de no ser así retorna -1.
        """
        if (key == None):
            return self.__search_prim(value)
        if self.__is_dict():
            return self.__search_dict(value, key)
        else:
            return self.__search_obj(value, key)

    def appendUnique(self, value):
        """
        Añade un valor al final de la lita actual sólo si no existe ya.

        Args:
            -`value`: El valor a añadir
        """
        if not (value in self):
            self.append(value)
        

    def __approach_or_key(self, value):
        if (type(value) == type(str())):
            return True
        return False
            
    def __max_dict(self, key):
        maximo = 0
        posicion = 0
        for index, item in enumerate(self):
            if not (self.__approach_or_key(key)):
                if (key(item) > maximo):
                    posicion = index
                    maximo = key(item)
            else:
                if (item[key] > maximo):
                    posicion = index
                    maximo = item[key]
        return posicion
        
    def __max_obj(self, attr):
        high = 0
        position = 0
        for index, item in enumerate(self):
            if hasattr(item, attr):
                value = getattr(item, attr)
                if (value > high):
                    high = value
                    position = index
        return position
        
    def max(self, key : str) -> int:
        """
        Retorna la posicion del elementos mal grande de una lista.

        Args:
            -`key`: La clave/atributo de cada `dict()` u `objeto` (TDA) que se ultizara para la comparacion.

        Returns:
            `int()`: La posicion del elemento mas grande de la lista.
        """
        if (self.__is_dict()):
            return self.__max_dict(key)
        else:
            return self.__max_obj(key)        
            
    def forEach(self, function):
        """
        Recorre la lista y aplica una función a cada elemento.
        
        Args:
            -`function`: La función que se aplicará a cada elemento de los datos. Esta `function` debe tomar un argumento (el elemento) y devolver un valor booleano.

        Returns:
            -`MyList`: Una nueva lista que contiene los elementos de los datos para los que la `function` ha devuelto `True`.
        """
        temp = MyList()
        for index, item in enumerate(self):
            if function(item):
                temp.append(item)
        return temp      
    
    def getOccurrences(self, key, *values):
        """Agrupa en una nueva lista los elementos determinados por un grupo de valores.

        Args:
            -`key`: La clave/atributo de cada `dict()` u `objeto` (TDA) que se ultizara para camparar.
            -`*values`: Grupo de valores que seran usados para comprar con cada elemento de la lista
            
        Returns:
            `MyList()`: Retorna una lista con las ocurrencias
        """
        temp = MyList()
        if self.__is_dict():
            for element in self:
                for ocurrrence in values:
                    if element[key] in ocurrrence:
                        temp.append((self, element))
            return temp
        else:
            for element in self:
                for ocurrrence in values:
                    if getattr(element, key) in ocurrrence:
                        temp.append(element)
            return temp
        
    
    def countOcurrencesForKey(self, key, *values):
        count = 0
        if not (self.__is_dict()):
            for index, item in enumerate(self):
                for value in values:
                    if (getattr(item, key) == value):
                        count += 1
            return count
        else:
            for index, item in enumerate(self):
                for value in values:
                    if (item[key] == value):
                        count += 1
            return count
        
    def AverageCalculator(self, key : str):
        """
        Determina el premdio de todos los elementos de la lista.

        Args:
            -`key`: La clave/atributo de cada `dict()` u `objeto` (TDA) que se ultizara para el calculo.

        Returns:
            -`float()`: retorna el promedio de los elementos
        """
        addition = 0
        if self.__is_dict():
            for index, item in enumerate(self):
                print(f"{item=}")
                addition = addition + item[key]
            return addition / len(self)
        else:
            for index, item in enumerate(self):
                addition = addition + getattr(item, key)
            return addition / len(self)
    

    def getDuplicates(self, key):
        """
        Agrupa los elementos que se repiten en una nueva lista y la retorna.

        Args:
            -`key`: La clave/atributo de cada `dict()` u `objeto` (TDA) que se ultizara para comparar.

        Returns:
            `MyList()`: Lista con los elementos duplicados
        """
        temp_list = []
        temp_res = MyList()
        if not self.__is_dict():
            for index, item in enumerate(self):
                if (getattr(item, key) in temp_list):
                    temp_res.append(getattr(item, key))    
                temp_list.append(getattr(item, key))
            return temp_res   

                
    
    def __str__(self):
        return '[\n' + ', \n'.join(f"    {str(item)}" for item in self) + '\n]'