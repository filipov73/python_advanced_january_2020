rows, columns = [int(x) for x in input().split(", ")]

matrix_sum_columns = [0 for _ in range(columns)]

for _ in range(rows):
    line = [int(x) for x in input().split(" ")]
    matrix_sum_columns = [sum(x) for x in zip(line, matrix_sum_columns)]


print("\n".join(map(str, matrix_sum_columns)))


#
# def sum_(f, s):
#     return f + s
#
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# print(list(map(sum_, a, b)))
