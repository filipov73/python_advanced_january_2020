def explode(row, column, matrix, bombs):
    value = matrix[row][column]
    size = len(matrix[0])
    if value > 0:
        for row_idx in range(row - 1, row + 1 + 1):
            for col_idx in range(column - 1, column + 1 + 1):
                if row != row_idx or column != col_idx:
                    if in_matrix(row_idx, col_idx, size):
                        if matrix[row_idx][col_idx] > 0:
                            matrix[row_idx][col_idx] -= value
        matrix[row][column] = 0
    return matrix


def in_matrix(row_1, col_1, size):
    # if 0 <= row_1 < size and 0 <= col_1 < size:
    #     return True
    # return False
    return 0 <= row_1 < size and 0 <= col_1 < size

num = int(input())
matrix = []
for _ in range(num):
    line = [int(x) for x in input().split()]
    matrix.append(line)

bombs = []
line = [x for x in input().split()]
for bomb in line:
    r_c = [int(x) for x in bomb.split(",")]
    bombs.append(r_c)




for r_c in bombs:
    row = r_c[0]
    column = r_c[1]
    explode(row, column, matrix, bombs)

count_alive_cells = 0
sum_of_cells = 0
alive_cells = []
for line in matrix:
    alive_cells = [x for x in line if x > 0]
    count_alive_cells += len(alive_cells)
    sum_of_cells += sum(alive_cells)
print(f"Alive cells: {count_alive_cells}")
print(f"Sum: {sum_of_cells}")

# for line in matrix:
#     print(" ".join(map(str, line)))
[print(*row) for row in matrix]


