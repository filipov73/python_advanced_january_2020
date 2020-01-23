size_matrix = int(input())

martix = []
sum_diagonal = 0
for i in range(size_matrix):
    line = [int(x) for x in input().split()]
    sum_diagonal += line[i]
    martix.append(line)
print(sum_diagonal)

# size_matrix = int(input())
#
# martix = []
# sum_diagonal = 0
# for i in range(size_matrix):
#     line = [int(x) for x in input().split()]
#     # sum_diagonal += line[i]
#     martix.append(line)
#
# for i in range(size_matrix):
#     sum_diagonal += martix[i][i]
# print(sum_diagonal)
