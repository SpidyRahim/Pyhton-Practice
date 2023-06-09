numbers = [1, 2, 3, 4, 8, 9, 10, 5, 6, 7]
numbers.append(11)
print(numbers)

numbers.insert(0, 99)
print(numbers)

numbers.pop(0)
print(numbers)


numbers.count(numbers)
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.count(10))

numbers.sort(key=None, reverse=False)
print(numbers)

numbers.clear()
print(numbers)

numbers.remove(1)
print(numbers)