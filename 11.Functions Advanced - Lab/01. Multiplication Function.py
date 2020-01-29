def multiply(n, *m):
    res = n
    for el in m:
        res *= el
    return res


print(multiply(1, 4, 5))
