import operator


def operate(str_operator, *m):
    dict_ = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result = m[0]
    for el in m[1:]:
        if el != 0 and operator != "/":
            result = dict_[str_operator](result, el)
        else:
            return
    return result


print(operate("*", 1, 2, 3))
print(operate("/", 8, 0))
