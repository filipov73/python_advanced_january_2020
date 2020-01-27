import sys

def read_matrix(size):
    matrix = []
    for _ in range(size):
        line = list(input())
        matrix.append(line)
    return matrix


def check_range_count(size, i, j):
    counter = 0
    if (0 <= i - 2 <= size - 1) and (0 <= j - 1 <= size - 1):
        if matrix[i - 2][j - 1] == "K":
            counter += 1
    if (0 <= i - 2 <= size - 1) and (0 <= j + 1 <= size - 1):
        if matrix[i - 2][j + 1] == "K":
            counter += 1
    if (0 <= i - 1 <= size - 1) and (0 <= j - 2 <= size - 1):
        if matrix[i - 1][j - 2] == "K":
            counter += 1
    if (0 <= i - 1 <= size - 1) and (0 <= j + 2 <= size - 1):
        if matrix[i - 1][j + 2] == "K":
            counter += 1
    if (0 <= i + 1 <= size - 1) and (0 <= j - 2 <= size - 1):
        if matrix[i + 1][j - 2] == "K":
            counter += 1
    if (0 <= i + 1 <= size - 1) and (0 <= j + 2 <= size - 1):
        if matrix[i + 1][j + 2] == "K":
            counter += 1
    if (0 <= i + 2 <= size - 1) and (0 <= j - 1 <= size - 1):
        if matrix[i + 2][j - 1] == "K":
            counter += 1
    if (0 <= i + 2 <= size - 1) and (0 <= j + 1 <= size - 1):
        if matrix[i + 2][j + 1] == "K":
            counter += 1
    return counter


size = int(input())
matrix = read_matrix(size)
max_count = -sys.maxsize - 1
target = []
removed = 0
while True:
    for i in range(size - 1):
        for j in range(size - 1):
            counter = 0
            if matrix[i][j] == "K":
                counter += check_range_count(size, i, j)
            if counter:
                if max_count < counter:
                    max_count = counter
                    target = [i, j]
                    # removed += 1
    if target:
        matrix[target[0]][target[1]] = "0"
        removed += 1
    if not max_count:
        break
    max_count = 0
    target = []


print(removed)
print(matrix)
