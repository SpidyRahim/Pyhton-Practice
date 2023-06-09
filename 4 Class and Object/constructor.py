class Phone:
    manufactured = 'China'

    # constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, Phone_Number, SMS):
        text = f'Sending SMS to : {Phone_Number} an Message : {SMS}'
        print(text)


my_phone = Phone('Rahim', 'Xiaomi', 19000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('She', 'Samsung', 130000)
print(her_phone.owner, her_phone.brand, her_phone.price)

dad_phone = Phone('Monir Hosain', 'Iphone', 190000)
print(dad_phone.owner, dad_phone.brand, dad_phone.price)
