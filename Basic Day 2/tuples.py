def multiple():
    return 3, 4
# print(multiple())


things = 'pen', 'tripod', 'water', 'phone', 'sunglass'
# print(type(things)) bujhacche j ekhane tuple ache

# print(things[0]) prothom pen ta amra reach korte parlam
# print(things[-2]) pichon theke amra phone ta reach korte parlam karon phone -2 position e ache
# print(things[1:4]) slice kore tuple er maan gula pailam

if 'phone' in things:
    print('Achi re vai achi')

if 'water bottle' not in things:
    print('Nai re vai')

# things[0] = 'wagon'
# print(things) possible na karon tuple hoccche immutable

# duita list ek sathe jora lagiye tuple banalam
mega = ([1, 2, 3, 4], [5, 6, 7, 8])
print(type(mega))

# ekhane amra 0 diye prothom tuple then 1 diye oi list er 1 number index er value ta manipulate korechi
mega[0][1] = 666
print(mega)
