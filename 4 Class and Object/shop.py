class Shop:
    # eta class attribute eta sobar sathe share hoy protthek ta instence er sathe
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

Ritu = Shop('Ritu')
Ritu.add_to_cart('Apple Watch')
Ritu.add_to_cart('IPhone')
Ritu.add_to_cart('IPad')
Ritu.add_to_cart('IPod')

print(Ritu.cart)

Rahim = Shop('Rahim')
Rahim.add_to_cart('Mi Band')
Rahim.add_to_cart('Xiaomi')
Rahim.add_to_cart('Car')
Rahim.add_to_cart('Bike')

print(Rahim.cart)