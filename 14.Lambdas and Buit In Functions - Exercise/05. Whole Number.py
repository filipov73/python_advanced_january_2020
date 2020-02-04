numbers = [float(x) for x in input().split()]
numbers_round = [round(x) for x in numbers]
length = len(numbers)
print(sum(numbers_round) * length)
