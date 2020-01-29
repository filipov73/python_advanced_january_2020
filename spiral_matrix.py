def in_range(value, max_value):
    return 0 <= value < max_value


n = 6

row_dirs = [0, +1, 0, -1]
col_dirs = [+1, 0, -1, 0]

matrix = [[None] * n for _ in range(n)]
dir_ = 0
row = 0
col = 0

for count in range(n * n):
    matrix[row][col] = count + 1
    next_row = row + row_dirs[dir_]
    next_col = col + col_dirs[dir_]
    if not in_range(next_row, n) \
            or not in_range(next_col, n) \
            or matrix[next_row][next_col]:
        dir_ += 1
        dir_ %= 4
    row += row_dirs[dir_]
    col += col_dirs[dir_]


for row in matrix:
    for i in range(len(row)):
        print(f"{row[i]:3d}", end="")
    print()
