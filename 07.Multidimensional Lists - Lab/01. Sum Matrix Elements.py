rows, columns = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix_sum += sum(line)
    matrix.append(line)

print(matrix_sum)
print(matrix)
