""" def all_sum(*numbers):
    print(numbers)


all_sum(45, 10, 20, 30) """


def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0

    for num in numbers:
        print(num)
        sum += num
    return sum


total = all_sum(45, 10, 100, 30)
print("Sum is = ", total)
