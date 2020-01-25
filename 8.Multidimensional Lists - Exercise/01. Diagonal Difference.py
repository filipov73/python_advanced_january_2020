size = int(input())

matrix = [list(map(int, input().split())) for _ in range(size)]

diagonal_sum_1 = 0
diagonal_sum_2 = 0
for i in range(size):
    diagonal_sum_1 += matrix[i][i]
a = 0
for i in range(size - 1, -1, -1):
    diagonal_sum_2 += matrix[a][i]
    a += 1

print(abs(diagonal_sum_1 - diagonal_sum_2))
