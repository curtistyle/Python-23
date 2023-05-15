from decimal import Decimal

class Acount():
    
    def __init__(self, name, balance):
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money to the acount."""
        
        # if amount is less than 0.00, raise an exeption
        if amount < Decimal('50.00'):
            raise ValueError('amount must be positive.')
        self.balance += amount


#acount1 = Acount('John Green', Decimal('50.00'))



