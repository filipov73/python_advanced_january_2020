def make_matrix(input, rows, columns):
    pass


rows, columns = [int(x) for x in input().split(", ")]

matrix = []
big_matrix = []
current_martix = []
current_sum = 0
big_sum = 0
for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

for i in range(rows-1):
    for j in range(columns-1):
        current_martix.append(matrix[i][j])
        current_martix.append(matrix[i][j + 1])
        current_martix.append(matrix[i + 1][j])
        current_martix.append(matrix[i + 1][j + 1])
        current_sum = sum(current_martix)
        if current_sum > big_sum:
            big_sum = current_sum
            big_matrix = current_martix
        current_martix = []
        current_sum = 0
a = 1
for i in big_matrix:
    print(i, end=" ")
    if a == 2:
        a = 0
        print()
    a += 1
print(big_sum)
