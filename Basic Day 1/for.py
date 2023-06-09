# numbers = [1, 2, 3]

# for i in numbers:
#     print(i)


# numbers = [1, 2, 3]
# sum = 0
# for i in numbers:
#     print(i)
#     sum += 1
# print("Sum is :", sum)


# for i in range(1, 11):
#     print(i, 'i am')


# Sample array
arr = [10, 20, 30, 40, 50]

# # Element to search
# search_element = 50

# # Iterate over the array using enumerate()
# for index, element in enumerate(arr):
#     if element == search_element:
#         print("Element", search_element, "found at index", index)
#         break  # Exit the loop once the element is found

# # Output: Element 30 found at index 2


arr = ['Jab', 'Rahim', 'Met', 'Boss']

search_text = input() # ekhane amra text input hisebe nicchi pore jate amra eta kothay array te ache ta dekhte

for index, element in enumerate(arr):
    if element == search_text:
        print("The Text -> ", search_text, "found at index :", index)
        break
