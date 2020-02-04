def get_magic_triangle(n):
    result_list = [[1]]
    for row in range(1, n):
        current = []
        current.append(1)
        for idx in range(1, len(result_list[row-1])):
            current.append(result_list[row-1][idx-1] + result_list[row-1][idx])

        current.append(1)
        result_list.append(current)

    return result_list


print(get_magic_triangle(5))
