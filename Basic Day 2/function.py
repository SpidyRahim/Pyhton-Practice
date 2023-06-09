def double_it(num):
    result = num*2
    # print(result)
    return result


#double_it(10)

# double_it(100)


def sum_it(num1, num2):
    results = num1 + num2
    # print(results)
    return results


# sum_it(10, 40)

total = double_it(sum_it(10, 10))
print('Total is : ', total)
