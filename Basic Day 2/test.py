# N = int(input())
# A = list(map(int, input().split()))

# max_operations = 0

# while all(num % 2 == 0 for num in A):
#     A = [num // 2 for num in A]
#     max_operations += 1

# print(max_operations)


# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# count_dict = {}

# for num in A:
#     count_dict[num] = count_dict.get(num, 0) + 1

# for i in range(1, M+1):
#     count = count_dict.get(i, 0)
#     print(count)


# class Person:
#     def __init__(self, name, age, height, weight) -> None:
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight


# class Cricketer(Person):
#     def __init__(self, name, age, height, weight) -> None:
#         super().__init__(name, age, height, weight)

#     def __lt__(self, other):
#         return self.age < other.age


# Sakib = Cricketer('Sakib', 38, 68, 91)
# Mushfiq = Cricketer('Mushfiq', 36, 55, 82)
# Mustafiz = Cricketer('Mustafiz', 27, 69, 86)
# Riyad = Cricketer('Riyad', 39, 72, 92)

# youngest_player = min([Sakib, Mushfiq, Mustafiz, Riyad])

# print(youngest_player.name)


# class Animal:
#     def __init__(self):
#         print("This is an animal.")

#     def eat(self):
#         print("The animal is eating.")


# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("This is a dog.")

#     def bark(self):
#         print("The dog is barking.")


# class Bulldog(Dog):
#     def __init__(self):
#         super().__init__()
#         print("This is a bulldog.")

#     def snore(self):
#         print("The bulldog is snoring.")


# bulldog = Bulldog()
# bulldog.eat()
# bulldog.bark()
# bulldog.snore()


# class Car:
#     def __init__(self, fuel_level, miles_traveled):
#         self.fuel_level = fuel_level
#         self.miles_traveled = miles_traveled

#     def calculate_fuel_efficiency(self):
#         def _calculate_mpg():
#             return self.miles_traveled / self.fuel_level

#         return f"The car gets {_calculate_mpg()} miles per gallon."


# class Dog:
#     def speak(self):
#         def _generate_sound():
#             return "Woof!"

#         return f"The dog says {_generate_sound()}"


# class Cat:
#     def speak(self):
#         def _generate_sound():
#             return "Meow!"

#         return f"The cat says {_generate_sound()}"


# def sum_of_squares(numbers):
#     def _square(x):
#         return x ** 2

#     return sum(_square(x) for x in numbers)

# class MyClass:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def sum(self):
#         return self.a + self.b + self.c

#     def factorial(self):
#         result = 1
#         for i in range(2, self.b+1):
#             result *= i
#         return result


# class Shape:
#     @staticmethod
#     def calculate_area():
#         print("This shape doesn't have a defined area")


# class Circle(Shape):
#     @staticmethod
#     def calculate_area(radius):
#         area = 3.14 * (radius ** 2)
#         print(f"The area of the circle is {area}")


# class Rectangle(Shape):
#     @staticmethod
#     def calculate_area(length, width):
#         area = length * width
#         print(f"The area of the rectangle is {area}")


# # call the calculate_area() method on each subclass
# Shape.calculate_area()         # This shape doesn't have a defined area
# Circle.calculate_area(5)       # The area of the circle is 78.5
# Rectangle.calculate_area(4, 5)  # The area of the rectangle is 20


# class Animal:
#     def make_sound(self):
#         print("The animal makes a sound")


# class Dog(Animal):
#     def make_sound(self):
#         print("The dog barks")


# class Cat(Animal):
#     def make_sound(self):
#         print("The cat meows")


# # create instances of the classes
# animal = Animal()
# dog = Dog()
# cat = Cat()

# # call the make_sound() method on each instance
# animal.make_sound()  # The animal makes a sound
# dog.make_sound()     # The dog barks
# cat.make_sound()     # The cat meows


# class MyBaseClass:
#     @staticmethod
#     def my_static_method():
#         print("Base class's static method")


# class MySubClass(MyBaseClass):
#     pass


# MySubClass.my_static_method()  # Output: Base class's static method


# class MyBaseClass:
#     @classmethod
#     def my_class_method(cls):
#         print("Base class's class method")


# class MySubClass(MyBaseClass):
#     @classmethod
#     def my_class_method(cls):
#         print("Subclass's class method")


# MySubClass.my_class_method()  # Output: Subclass's class method

# class MyClass:
#     my_class_attribute = 42

#     @classmethod
#     def my_class_method(cls):
#         print("Class attribute value:", cls.my_class_attribute)


# MyClass.my_class_method()  # Output: Class attribute value: 42


# class MyClass:
#     my_class_attribute = 42

#     @staticmethod
#     def my_static_method():
#         # Raises AttributeError
#         print("Class attribute value:", MyClass.my_class_attribute)


# MyClass.my_static_method()


# class MyClass:
#     @classmethod
#     def my_class_method(cls, arg1, arg2):
#         print("Class method called with arguments:", arg1, arg2)


# # Output: Class method called with arguments: 10 20
# MyClass.my_class_method(10, 20)

class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        print("Static method called with arguments:", arg1, arg2)


# Output: Static method called with arguments: 30 40
MyClass.my_static_method(30, 40)
