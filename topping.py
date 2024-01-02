class Topping:
    # __slots__ = ('__cheese', '__meat', '__veggies')

    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.price}"
        
    
