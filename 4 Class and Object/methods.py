def call():
    print('Calling Someone')


class Phone:
    price = 19000
    color = 'Black'
    brand = 'Xiaomi'
    feature = ['camera', 'speaker', 'ir blaster']

# self diye nilam karon prothomoto ekta parameter pass kora lagbe (Class er vitor) sei khetre prothom ta amra default perameter hisebe niye nilam like as "self"
    def call(self):
        print('Calling One Person')

    def send_sms(self, Phone_Number, Message):
        text = f'Sending SMS to : {Phone_Number} an Message : {Message}'
        return text


my_phone = Phone()
print(my_phone.feature)
my_phone.call()


result = my_phone.send_sms('01712705974', 'Hello Text Form BOT')
print(result)
