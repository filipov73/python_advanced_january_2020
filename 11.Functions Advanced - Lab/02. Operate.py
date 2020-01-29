import operator


def operate(str_operator, n, *m):
    dict_ = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result = n
    for el in m:
        if el != 0 and str_operator != "/":
            result = dict_[str_operator](result, el)

    return result


print(operate("*", 1, 2, 3))
print(operate("/", 8, 0))
