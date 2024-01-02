class Pizza:
    def __init__(self, cheeses, meats, veggies, price):
        self.cheeses = cheeses
        self.meats = meats
        self.veggies = veggies
        self.price = price

    def calculate_price(self):
        for i in (self.cheeses):
            self.price += i.price
        for i in (self.meats):
            self.price += i.price
        for i in (self.veggies):
            self.price += i.price
        return self.price

    def name_list(self, list):
        names = []
        for i in list:
            names.append(i.name)
        return names
    
    def get_price(self):
        return self.price

    def __str__(self):
        self.calculate_price()
        names_Ch = self.name_list(self.cheeses)
        names_Mt = self.name_list(self.meats)
        names_Vg = self.name_list(self.veggies)
        return f"cheeses: {names_Ch}, meats: {names_Mt}, veggies: {names_Vg}, price: {self.price}"
        