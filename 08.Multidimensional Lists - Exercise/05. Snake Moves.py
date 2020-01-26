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
snack_string = list(input())
idx = 0
rows_count = len(matrix)
columns_count = len(matrix[0])
while True:
    if idx >= len(snack_string):
        idx = 0
    print(idx)
    print(snack_string[idx])
    idx += 1

print_matrix(matrix)
