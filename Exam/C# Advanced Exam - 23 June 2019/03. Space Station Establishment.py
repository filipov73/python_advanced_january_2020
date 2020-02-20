def create_galaxy(num, matrix):
    for _ in range(num):
        matrix.append([x for x in input()])
    return matrix


def check_position_in_galaxy(row, col, size):
    if 0 <= row < 3 and 0 <= col < size:
        return True
    return False


def find_stephen(matrix):
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == "S":
                return row_idx, col_idx


def find_holes(matrix):
    holes = []
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix)):
            if matrix[row_idx][col_idx] == "O":
                holes.append([row_idx, col_idx])
    return holes


def move_stephen(row, col, command):
    move = {
        "up": [-1 + row, 0 + col],
        "down": [1 + row, 0 + col],
        "left": [0 + row, -1 + col],
        "right": [0 + row, 1 + col],
    }
    return move[command]


size = int(input())
galaxy = []
create_galaxy(size, galaxy)
star_power = 0
void = False

position_stephen = find_stephen(galaxy)
position_holes = find_holes(galaxy)
command = input()
while True:
    current_position_stephen = move_stephen(*position_stephen, command)
    if not check_position_in_galaxy(*current_position_stephen, size):
        galaxy[position_stephen[0]][position_stephen[1]] = "-"
        void = True
        break
    galaxy[position_stephen[0]][position_stephen[1]] = "-"
    if current_position_stephen in position_holes:
        galaxy[current_position_stephen[0]][current_position_stephen[1]] = "-"
        position_holes.pop(position_holes.index(current_position_stephen))
        current_position_stephen = position_holes[0]
    elif galaxy[current_position_stephen[0]][current_position_stephen[1]].isdigit():
        power = int(galaxy[current_position_stephen[0]][current_position_stephen[1]])
        star_power += power
    position_stephen = current_position_stephen
    galaxy[position_stephen[0]][position_stephen[1]] = "S"
    if star_power >= 50:
        break
    command = input()


if void:
    print("Bad news, the spaceship went to the void.")
if star_power >= 50:
    print("Good news! Stephen succeeded in collecting enough star power!")

print(f"Star power collected: {star_power}")
for line in galaxy:
    print("".join(map(str, line)))



