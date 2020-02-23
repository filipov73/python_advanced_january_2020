def read_matrix(size_matrix):
    rez = []
    for row in range(size_matrix):
        rez.append(input().split())
    return rez

def start_position(matrix):
    length = len(matrix[0])
    position = []
    count = 0
    for row_idx in range(length):
        for column_idx in range(length):
            if matrix[row_idx][column_idx] == "p":
                position = [row_idx, column_idx]
            if matrix[row_idx][column_idx] == "t":
                count += 1
    return position, count

def is_valid(matrix, position):
    size = len(matrix[0])
    if 0 <= position[0] < size and 0 <= position[1] < size:
        if matrix[position[0]][position[1]] == ".":
            return True
    return False


def is_valid1(matrix, position):
    size = len(matrix[0])
    if 0 <= position[0] < size and 0 <= position[1] < size:
        return True
    return False

def move_player(matrix,position, command, step):
    current_position = position
    player_move = {
        "up": [-step, 0],
        "down": [step, 0],
        "left": [0, -step],
        "right": [0, step]
    }
    new_position = current_position[0] + player_move[command][0], current_position[1] + player_move[command][1]
    if is_valid(matrix, new_position):
        matrix[new_position[0]][new_position[1]] = "p"
        matrix[current_position[0]][current_position[1]] = "."

        return matrix, new_position
    return matrix, current_position


def shoot(matrix, position, command, step):
    player_move = {
        "up": [-step, 0],
        "down": [step, 0],
        "left": [0, -step],
        "right": [0, step]
    }
    target_position = position[0] + player_move[command][0], position[1] + player_move[command][1]
    if is_valid1(matrix, target_position):
        if matrix[target_position[0]][target_position[1]] == "t":
            matrix[target_position[0]][target_position[1]] = "x"
            return matrix
        matrix[target_position[0]][target_position[1]] = "x"
    return matrix


rows = int(input())
matrix = read_matrix(rows)
position, count = start_position(matrix)

num = int(input())

for _ in range(num):
    command = input().split()
    current_position = position
    if command[0] == "move":
        move_command = command[1]
        step = int(command[2])
        matrix, current_position = move_player(matrix, current_position, move_command, step)

    elif command[0] == "shoot":
        move_command = command[1]
        step = int(command[2])
        matrix = shoot(matrix, current_position, move_command, step)

    elif command[0] == "":
        pass
    position, new_count = start_position(matrix)
    if new_count == 0:
        break
    position = current_position

# •	move {right/left/up/down} {steps} - the plane moves in the given direction with the given steps. Move the player only if the filed he wants to step on is marked with "."
# •	shoot {right/left/up/down} {steps} - the plane shoots in the given direction with the given steps (from his current position without moving), the field gets destroyed and marked with a "x". If the plane shoots at a target, it also gets destroyed. When a field is destroyed, the plane can no longer step on it.
# •	Validate the positions, since they can be outside the field




position, new_count = start_position(matrix)
if new_count == 0:
    print(f"Mission accomplished! All {count} targets destroyed.")
else:
    print(f"Mission failed! {new_count} targets left.")

for line in matrix:
    print(" ".join(line))