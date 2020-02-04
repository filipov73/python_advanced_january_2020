numbers = [float(x) for x in input().split()]

round_numbers = sorted(set(map(round, numbers)))

print(min(round_numbers))
print(max(round_numbers))
mul_x_3 = [x * 3 for x in round_numbers]
print(" ".join(map(str, mul_x_3)))


# min and max and multiply the numbers by 3.
# Print only the unique numbers in ascending order separated by space

