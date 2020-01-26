size = int(input())
matrix = [list(input()) for x in range(size)]
search = input()
target = False
row_col = []

for i in range(size):
    for j in range(size):
        if search == matrix[i][j]:
            row_col.append(i)
            row_col.append(j)

            target = True


if not target:
    print(f"{search} does not occur in the matrix")
else:
    print(f"({row_col[0]}, {row_col[1]})")
