import sys

def read_matrix():
    (rows_count, columns_count) = [int(x) for x in input().split()]
    matrix_ = []
    for _ in range(rows_count):
        line = [int(x) for x in input().split()]
        matrix_.append(line)
    return matrix_


def sub_matrix(matrix, row_idx, column_idx):
    ROW_COL = 3
    row_idx = row_idx
    column_idx = column_idx
    n = len(matrix)
    sub_matrix = []
    for i in range(ROW_COL):
        el = matrix[row_idx + i][column_idx:column_idx + ROW_COL]
        sub_matrix.append(el)

    return sub_matrix

def sub_matrix_sum(matrix):
    sums = 0
    for row in matrix:
        sums += sum(row)
    return sums


def search(matrix):
    ROW_COL = 3
    # sub_matrix = []

    the_best_sum = -sys.maxsize -1

    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for i in range(rows_count - ROW_COL + 1):
        for j in range(columns_count - ROW_COL + 1):

            sub_matrix_ = sub_matrix(matrix, i, j)
            sums = sub_matrix_sum(sub_matrix_)
            if the_best_sum < sums:
                the_best_sum = sums
                the_best_matrix = sub_matrix_


    return the_best_sum, the_best_matrix



matrix = read_matrix()
search(matrix)


the_best_sum, the_best_matrix = search(matrix)
print(f"Sum = {the_best_sum}")
# print("\n".join(map(str, the_best_matrix)))
for line in the_best_matrix:
    print(" ".join(map(str, line)))
