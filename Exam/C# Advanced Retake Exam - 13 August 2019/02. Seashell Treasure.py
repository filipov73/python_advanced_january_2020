def check_position_in_matrix(row, col, matrix):
    # length_row = len(matrix)
    # length_col = len(matrix[row])
    # if 0 <= row < length_row and 0 <= col < length_col:
    #     return True
    # return False
    try:
        a = matrix[row][col]
        return True
    except IndexError:
        return False


def check_and_replace(row, col, matrix):
    if matrix[row][col] != "-":
        shell = matrix[row][col]
        matrix[row][col] = "-"
        return shell


def seagull_gully_new_position(row, col, matrix, direction):
    direction_dict = {
        "up": [[-1+row, col], [-2+row, col], [-3+row, col]],
        "down": [[1+row, col], [2+row, col], [3+row, col]],
        "left": [[row, -1+col], [row, -2+col], [row, -3+col]],
        "right": [[row, 1+col], [row, 2+col], [row, 3+col]],
    }
    return direction_dict[direction]

    # row, col = row + direction_dict[direction][0], col + direction_dict[direction][1]
    #
    # if check_position_in_matrix(row, col, matrix):
    #     return row, col


numbers = int(input())

my_seashells = []
seagull_gully_seashells = []

beach_matrix = []
for _ in range(numbers):
    beach_matrix.append([line for line in input().split()])


command = input()
while command != "Sunset":
    token = command.split()
    if token[0] == "Collect":
        row = int(token[1])
        col = int(token[2])
        if check_position_in_matrix(row, col, beach_matrix):
            shell = check_and_replace(row, col, beach_matrix)
            if shell is not None:
                my_seashells.append(shell)
    elif token[0] == "Steal":
        row = int(token[1])
        col = int(token[2])
        direction = token[3]
        if check_position_in_matrix(row, col, beach_matrix):
            shell = check_and_replace(row, col, beach_matrix)
            if shell is not None:
                seagull_gully_seashells.append(shell)
                new_3_positions = seagull_gully_new_position(row, col, beach_matrix, direction)
                if new_3_positions is not None:
                    row, col = new_3_positions
                    shell = check_and_replace(row, col, beach_matrix)
                    if shell is not None:
                        seagull_gully_seashells.append(shell)
    command = input()

for line in beach_matrix:
    print(" ".join(line))

my_seashells_list = f"{', '.join(my_seashells)}"
print(f"Collected seashells: {len(my_seashells)}", end="")
if my_seashells:
    print(f" -> {my_seashells_list}")
else:
    print()
print(f"Stolen seashells: {len(seagull_gully_seashells)}")

