from list import MyList

class Pokemon():
    def __init__(self, name, level, type, subtype) -> None:
        self.name  = name
        self.level = level
        self.type = type
        self.subtype = subtype
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (type(value) == type(str())):
            raise ValueError(f"{value=} must be {type(str())} type.")
        self._name = value
        
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not (type(value) == type(int())):
            raise ValueError(f"{value=} must be {type(int())} type.")
        self._level = value
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        if not (type(value) == type(str())):
            raise ValueError(f"{value=} must be {type(str())} type.")
        self._type = value
        
    @property
    def subtype(self):
        return self._subtype
    
    @subtype.setter
    def subtype(self, value):
        
        if (type(value) == type(int())):
            raise ValueError(f"{value=} must be {type(str())} type.")
        self._subtype = value
    
    def getAllType(self):
        """return a list with type and subtype of the pokemon"""
        return MyList([self.type, self.subtype])
    
    def __repr__(self) -> str:
        return f"Pokemon(name={self.name}, level={self.level}, type={self.type}, subtype={self.subtype})"
    
    def __str__(self) -> str:
        return f"'{self.name}' is level '{self.level}' and his type is '{self.type}' and subtype '{self.subtype}'."
    
    

    
    