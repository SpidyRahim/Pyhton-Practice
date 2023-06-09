class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'Items': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)

    def remove_from_cart(self, item):
        for product in self.cart:
            if product['Items'] == item:
                self.cart.remove(product)
                print(f'{item} removed from the cart')
                break

        else:
            print(f'{item} not found in the cart')

    def checkout(self, amount):
        total = 0
        for all_items in self.cart:
            total += all_items['Price'] * all_items['Quantity']
        print('Total Price :', total)

        if amount < total:
            print(f'Please Give {total - amount} More Money')

        else:
            print(
                f'Here is your desire items and you change is {amount - total}')


rahim = Shopping('Rahim')
rahim.add_to_cart('Watch', 1000, 1)
rahim.add_to_cart('Pen', 10, 2)
rahim.add_to_cart('Book', 500, 1)
rahim.add_to_cart('TV', 40000, 1)

# print(rahim.cart)
rahim.checkout(50000)
rahim.remove_from_cart('TV')
rahim.checkout(500000)
