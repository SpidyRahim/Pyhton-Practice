numbers = [45, 42, 43, 29, 86, 14, 51, 62, 75, 98, 23, 57, 41, 68, 32, 94, 19, 76, 38, 45, 81, 37, 66, 12, 49,
           83, 27, 59, 88, 16, 72, 34, 67, 92, 26, 53, 79, 35, 61, 97, 21, 74, 46, 63, 85, 31, 55, 89, 13, 69, 84, 22, 58]
odds = []
evens = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
    if num % 2 == 0:
        evens.append(num)
print(odds)
print(evens)


odd_numbers = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
print(odd_numbers)

evens_numbers = [num for num in numbers if num % 2 == 0]
print(evens_numbers)
