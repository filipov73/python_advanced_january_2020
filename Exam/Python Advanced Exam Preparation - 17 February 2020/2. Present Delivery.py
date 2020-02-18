def find_santa(matrix):
    length = len(matrix[0])
    for row_idx in range(length):
        for column_idx in range(length):
            if matrix[row_idx][column_idx] == "S":
                return [row_idx, column_idx]


def is_valid(position, size):

    if 0 <= position[0] < size and 0 <= position[1] < size:
        return True
    return False


def move_santa(com, pos):
    global size_matrix
    santa_move = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1]
    }
    if is_valid([x+y for x, y in zip(santa_move[com], pos)], size_matrix):
        return [x+y for x, y in zip(santa_move[com], pos)]
    return pos


presents = int(input())
size_matrix = int(input())
nice_kids = 0
ex = False


matrix = []
[matrix.append(input().split()) for _ in range(size_matrix)]
santa_position = find_santa(matrix)
# santa_move = {
#     "up": [-1, 0],
#     "down": [1, 0],
#     "left": [0, -1],
#     "right": [0, 1]
# }


command = input()

while command != "Christmas morning":
    current_row, current_column = move_santa(command, santa_position)
    matrix[santa_position[0]][santa_position[1]] = "-"
    if matrix[current_row][current_column] == "V":
        presents -= 1
        nice_kids += 1
        matrix[current_row][current_column] = "S"
    elif matrix[current_row][current_column] == "C":
        for move in ["up", "down", "left", "right"]:
            row, column = move_santa(move, (current_row, current_column))
            if matrix[row][column] == "V" or matrix[row][column] == "X":
                matrix[row][column] = "-"
                presents -= 1
                nice_kids += 1
                # if presents == 0:
                #     ex = True
                #     break
        matrix[current_row][current_column] = "S"
        # if ex:
        #     break
    else:
        matrix[current_row][current_column] = "S"

    santa_position = (current_row, current_column)
    if presents == 0:
        break
    command = input()

counter = 0
for line in matrix:
    counter += len([x for x in line if x == "V"])
if presents == 0 and counter:
    print("Santa ran out of presents!")
[print(*line) for line in matrix]


if counter > 0:
    print(f"No presents for {counter} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")

# def read_matrix(size_matrix):
#
#     return [[x for x in input().split()] for _ in range(size_matrix)]
#
#
# def find_santa(matrix):
#     length = len(matrix[0])
#     for row_idx in range(length):
#         for column_idx in range(length):
#             if matrix[row_idx][column_idx] == "S":
#                 return [row_idx, column_idx]
#
#
# def move_santa(com, pos):
#     santa_move = {
#         "up": [-1, 0],
#         "down": [1, 0],
#         "left": [0, -1],
#         "right": [0, 1]
#     }
#     return [x+y for x, y in zip(santa_move[com], pos)]
#
#
# def happy_santa(nice_kids, presents, matrix, pos):
#     for com in ["up", "down", "left", "right"]:
#         row, column = move_santa(com, pos)
#         if matrix[row][column] == "V" or matrix[row][column] == "X":
#             matrix[row][column] = "-"
#             presents -= 1
#             nice_kids += 1
#     return nice_kids, presents, matrix
#
#
# def nice_kids_in_matrix(matrix):
#     counter = 0
#     for line in matrix:
#         counter += len([x for x in line if x == "V"])
#     return counter
#
#
# presents = int(input())
# size_matrix = int(input())
# nice_kids = 0
#
# matrix = read_matrix(size_matrix)
# santa_position = find_santa(matrix)
#
# command = input()
#
# while command != "Christmas morning":
#     current_santa_position = move_santa(command, santa_position)
#     row, column = current_santa_position
#
#     if matrix[row][column] == "V":
#         presents -= 1
#         nice_kids += 1
#     # elif matrix[row][column] == "X":
#     #     matrix[row][column] = "-"
#     elif matrix[row][column] == "C":
#         nice_kids, presents, matrix = happy_santa(nice_kids, presents, matrix, current_santa_position)
#     if presents <= 0:
#         matrix[santa_position[0]][santa_position[1]] = "-"
#         matrix[row][column] = "S"
#         break
#     matrix[santa_position[0]][santa_position[1]] = "-"
#     santa_position = [row, column]
#     matrix[row][column] = "S"
#     command = input()
#
#
# all_nice_kids_in_matrix = nice_kids_in_matrix(matrix)
# if all_nice_kids_in_matrix > 0:
#     print("Santa ran out of presents!")
# [print(*line) for line in matrix]
#
#
# if all_nice_kids_in_matrix > 0:
#     print(f"No presents for {all_nice_kids_in_matrix} nice kid/s.")
# else:
#     print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
