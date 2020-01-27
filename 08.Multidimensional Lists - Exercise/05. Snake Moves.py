def create_matrix():
    (rows, columns) = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows):
        line = [None]*columns
        matrix.append(line)
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print("".join(map(str, line)))


matrix = create_matrix()
snake_string = list(input())
idx = 0
idx_row = 0
idx_column = 0
rows_count = len(matrix)
columns_count = len(matrix[0])
while True:
    if idx >= len(snake_string):
        idx = 0
    matrix[idx_row][idx_column] = snake_string[idx]
    if idx_row % 2 == 0:

        if idx_row == rows_count - 1 and idx_column == columns_count - 1:
            break
    else:
        if idx_row == rows_count - 1 and idx_column == 0:
            break
    if idx_row % 2 == 0:
        if idx_column < columns_count - 1:
            idx_column += 1
        else:
            idx_row += 1

    else:
        if idx_column > 0:
            idx_column -= 1
        else:
            idx_row += 1

    idx += 1

print_matrix(matrix)
