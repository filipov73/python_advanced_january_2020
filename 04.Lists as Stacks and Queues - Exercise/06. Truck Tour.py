num = int(input())
start_idx = 0
fuel = 0
for idx in range(num):
    liter, kilometer = [int(x) for x in input().split(" ")]
    fuel += liter
    if fuel >= kilometer:
        fuel -= kilometer
    else:
        start_idx = idx + 1
        fuel = 0

print(start_idx)

