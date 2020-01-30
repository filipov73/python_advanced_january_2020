def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


# def func_executor(*m):
#     f = m[0][0](m[0][1][0], m[0][1][1])
#     s = m[1][0](m[1][1][0], m[1][1][1])
#     return [f, s]

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
