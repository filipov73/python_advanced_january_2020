def find_player_position(matrix):
    length = len(matrix[0])
    for row_idx in range(length):
        for column_idx in range(length):
            if matrix[row_idx][column_idx] == "P":
                return [row_idx, column_idx]


def is_valid_position(position):
    global size
    if 0 <= position[0] < size and 0 <= position[1] < size:
        return True
    return False


def move_player(command, position):
    player_move = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1]
    }
    current_position = [x+y for x, y in zip(player_move[command], position)]
    if is_valid_position(current_position):
        return current_position
    return position


string = input()
size = int(input())
matrix = []
for _ in range(size):
    matrix.append([ch for ch in input()])
num_command = int(input())
player_position = find_player_position(matrix)
for _ in range(num_command):
    command = input()
    matrix[player_position[0]][player_position[1]] = "-"
    current_player_position = move_player(command, player_position)
    if player_position == current_player_position:
        string = string[:-1]
    else:
        add_ch = matrix[current_player_position[0]][current_player_position[1]]
        if add_ch != "-":
            string += add_ch
    player_position = current_player_position
    matrix[player_position[0]][player_position[1]] = "P"
print(string)
for line in matrix:
    print("".join(line))
