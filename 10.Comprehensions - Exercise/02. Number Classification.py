num = [int(x) for x in input().split(", ")]

print(f"Positive: {', '.join(map(str, [x for x in num if x >= 0]))}")
print(f"Negative: {', '.join(map(str, [x for x in num if x < 0]))}")
print(f"Even: {', '.join(map(str, [x for x in num if x % 2 == 0]))}")
print(f"Odd: {', '.join(map(str, [x for x in num if x % 2 != 0]))}")


