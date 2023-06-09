class Shop:
    shoping_mall = []

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # eta instance attribute eta sobar sathe share hoy protthek ta instence er sathe

    def add_to_cart(self, cart):
        self.cart.append(cart)


Ritu = Shop('Ritu')
Ritu.add_to_cart('Apple Watch')
Ritu.add_to_cart('IPhone')
Ritu.add_to_cart('IPad')
Ritu.add_to_cart('IPod')

print(Ritu.cart)  # cart ta dekhte chai j ki ki ad korechi

Rahim = Shop('Rahim')
Rahim.add_to_cart('Mi Band')
Rahim.add_to_cart('Xiaomi')
Rahim.add_to_cart('Car')
Rahim.add_to_cart('Bike')

print(Rahim.cart)  # cart ta dekhte chai j ki ki ad korechi
