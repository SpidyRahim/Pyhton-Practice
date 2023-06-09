# pyhton forward ar backward 2 dik thekei array maintain korte pare

# index    0  1  2  3  4  5  6  7  8  9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1   ei j ulta vabaeo maintain kore

# print(numbers[3])

# # start theke end print kore [start(included):end(excluded)]
# print(numbers[3:9])


# # list [start : end : step]
# print(numbers[3:9:2])

# print(numbers[7:2:-1])  # ulta dik theke jabe


# print(numbers[7:2:-2])

print(numbers[4:])  # 4 theke shuru kore ekdom sesh obdi

print(numbers[:5])  # prothom theke shuru kore 5 er agg obdi jabe

# eta full list tai return kore dibe kono functionality nai kind of copy kora arki
print(numbers[:])

# reverse a list er shortcut hoilo nicher ta
print(numbers[::-1])
