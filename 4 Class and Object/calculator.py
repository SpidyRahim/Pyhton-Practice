class Calculator:
    Brand = 'Casio'

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def remainder(self, num1, num2):
        return num1 % num2


Cal = Calculator()

Adding = Cal.add(1, 2)
print(Adding)

Subtracting = Cal.subtract(1, 2)
print(Subtracting)

Multiplying = Cal.multiply(1, 2)
print(Multiplying)

Remainder = Cal.remainder(3, 2)
print(Remainder)
