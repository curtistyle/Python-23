# class Persona():
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
    
#     @property
#     def name(self):
#         return self._name


# persona1 = Persona("carlos", "alcaraz")

# #print(persona1.name)

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self._hour = hour # 0-23
        self._minute = minute # 0-59
        self._second = second # 0-59

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        
        self._hour = hour


time1 = Time(12,30,30)

print(time1.hour)

