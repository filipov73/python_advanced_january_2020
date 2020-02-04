def fix_calendar(calemdar):
    current = []
    while calemdar:
        for idx in range(len(calemdar)):
            if calemdar[0] > calemdar[idx]:
                calemdar[0], calemdar[idx] = calemdar[idx], calemdar
                # temp = calemdar[0]
                # calemdar[0] = calemdar[idx]
                # calemdar[idx] = temp
        current.append(calemdar.pop(0))

    return current


numbers = [3, 2, 1, 55, 100, 10]
fixed = fix_calendar(numbers)
print(fixed)
