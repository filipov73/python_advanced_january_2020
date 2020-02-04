command = input()
numbers = [int(x) for x in input().split()]
length = len(numbers)
result = 0


if command == 'Odd':
    result = sum([x * length for x in numbers if x % 2 == 1])
else:
    result = sum([x * length for x in numbers if x % 2 == 0])
print(result)
