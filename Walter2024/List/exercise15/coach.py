from pokemon import Pokemon
from list import MyList
class Coach():
    
    def __init__(self, name, tournaments_won, battles_won, battles_losses, pokemons) -> None:
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_won = battles_won
        self.battles_losses = battles_losses
        self.pokemons = pokemons
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not (type(value) == type(str())):
            raise ValueError(f"{value=} must be {type(str())} type")
        self._name = value
        
    @property
    def tournaments_won(self):
        return self._tournaments_won
    
    @tournaments_won.setter
    def tournaments_won(self, value):
        if not (type(value) == type(int())):
            raise ValueError(f"{value=} must be {type(int())} type")
        self._tournaments_won = value
    
    @property
    def battles_won(self):
        return self._battles_won
    
    @battles_won.setter
    def battles_won(self, value):
        if not (type(value) == type(int())):
            raise ValueError(f"{value=} must be {type(int())}type")
        self._battles_won = value
    
    @property
    def battles_losses(self):
        return self._battles_losses
    
    @battles_losses.setter
    def battles_losses(self, value):
        if not (type(value) == type(int())):
            raise ValueError(f"{value=} must be {type(int())}")
        self._battles_losses = value
    
    @property
    def pokemons(self):
        return self._pokemons
    
    @pokemons.setter
    def pokemons(self, value):
        if not (type(value) == type(MyList())):
            raise ValueError(f"{value=} must be {type(Pokemon())}")
        self._pokemons = value
    
    
    def __str__(self) -> str:
        return f"'{self.name}' win '{self.tournaments_won}' tournaments, {self.battles_won} battle won and {self.battles_losses} battle losses, their pokemons are: \n{self.pokemons}"
    