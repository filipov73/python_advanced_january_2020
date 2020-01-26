def read_martix():
    (rows, columns) = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows):
        line = [x for x in input().split()]
        if len(line) != columns:
            pass
        else:
            matrix.append(line)
    return matrix


def check_command(command, length):
    command = command.split()
    length = length
    if command[0] == "swap" and len(command) == 5:
        row_cell_1 = int(command[1])
        column_cell_1 = int(command[2])
        row_cell_2 = int(command[3])
        column_cell_2 = int(command[4])
        if 0 <= row_cell_1 <= length and \
            0 <= column_cell_1 <= length and \
            0 <= row_cell_2 <= length and \
            0 <= column_cell_2 <= length:
            return (row_cell_1, column_cell_1, row_cell_2, column_cell_2)
        else:
            return False
    else:
        return False


def print_matrix(matrix):
    matrix_ = matrix
    for i in matrix_:
        print(" ".join(map(str, i)))


matrix_ = read_martix()
command = input()

while True:
    if command == "END":
        break
    length = len(matrix_[0])
    comm = check_command(command, length)
    if comm:
        row_1, column_1, row_2, column_2 = comm
        temp = matrix_[row_2][column_2]
        matrix_[row_2][column_2] = matrix_[row_1][column_1]
        matrix_[row_1][column_1] = temp
        print_matrix(matrix_)
    else:
        print("Invalid input!")
    command = input()

