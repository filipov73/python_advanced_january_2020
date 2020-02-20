def find_player(matrix, player):
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == player:
                return row_idx, col_idx


def check_in_matrix(matrix, command, position):
    length = len(matrix)
    moves = {
        "up": [length - 1, 0],
        "down": [0, 0],
        "left": [0, length - 1],
        "right": [0, 0]
    }
    row, column = position
    if row < 0 or row >= length:
        row = moves[command][0]
    if column < 0 or column >= length:
        column = moves[command][1]
    return row, column


def move(matrix, command, position):
    moves = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1]
    }
    new_position = moves[command][0] + position[0], moves[command][1] + position[1]
    new_move_position = check_in_matrix(matrix, command,  new_position)
    return new_move_position

num = int(input())
matrix = [[x for x in input()] for _ in range(num)]

f_position = find_player(matrix, 'f')
s_position = find_player(matrix, 's')

while True:
    f_command, s_command = input().split()
    current_f_position = move(matrix, f_command, f_position)
    row, col = current_f_position
    if matrix[row][col] == "*":
        matrix[row][col] = "f"
    elif matrix[row][col] == "s":
        matrix[row][col] = "x"
        break
    f_position = (row, col)

    current_s_position = move(matrix, s_command, s_position)
    row, col = current_s_position
    if matrix[row][col] == "*":
        matrix[row][col] = "s"
    elif matrix[row][col] == "f":
        matrix[row][col] = "x"
        break
    s_position = (row, col)

for line in matrix:
    print("".join(line))
