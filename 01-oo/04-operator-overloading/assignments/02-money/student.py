class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")

        return (
            Money(self.amount + other.amount, self.currency)
        )
    
    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        
        return (
            Money(self.amount - other.amount, self.currency)
        )
    
    def __mul__(self, times_amount):
        if not isinstance(times_amount, (int, float)):
            raise TypeError("Multiplier must be an int or float")
            
        return (
            Money(self.amount*times_amount, self.currency)
        )
    
    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"
    
#print(Money(10, "EUR") + Money(20, "USD"))