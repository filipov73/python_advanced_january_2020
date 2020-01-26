def read_matrix():
    matrix = []
    (rows_count, columns_count) = map(int, input().split())
    for row in range(rows_count):
        line = [x for x in input().split()]
        matrix.append(line)

    return matrix, (rows_count, columns_count)


def equal_elements(matrix, size):
    rows_count, columns_count = size
    count_ = 0
    for i in range(rows_count - 1):
        for j in range(columns_count - 1):
            a = martix[i][j]
            b = martix[i][j+1]
            c = martix[i+1][j]
            d = martix[i+1][j+1]
            if a == b == c == d:
                count_ += 1
    return count_


martix, size = read_matrix()
count = equal_elements(martix, size)

print(count)
