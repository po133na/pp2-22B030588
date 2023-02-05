class Clothing:

    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        print(f'Name: {self.name}, size: {self.size}, color: {self.color}, price: {self.price}')

class Shirt(Clothing):

    def __init__(self, name, size, color, price, type):
        super().__init__(name, size, color, price)
        if type in ['casual', 'formal']:
            self.type = type
        else:
            print(f'Unknown')
    def display_info(self):
        print(f'Name: {self.name}, size: {self.size}, color: {self.color}, price: {self.price}')

shirt1 = Shirt(name = 'Shirt', size = 'S', color = 'white', price = 1000.0, type = 'unknown')
c = Clothing(name = 'Dress', size = 'S', color = 'white', price = 1000.0)
c.display_info()