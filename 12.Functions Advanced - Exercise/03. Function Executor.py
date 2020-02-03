def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2



def func_executor(*args):
    result = []
    for f in args:
        operation = f[0]
        f_num = f[1][0]
        s_num = f[1][1]
        r = operation(f_num, s_num)
        result.append(r)

    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
