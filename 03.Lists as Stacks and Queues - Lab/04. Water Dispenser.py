from collections import deque

water_dispenser = int(input())
name = input()

while name != "Start":
    name = input()

command = input()

while command != "End":
    token = command.split(" ")
    if len(token) == 1:
        liters = int(token[0])
        water_dispenser -= liters
    else:
        pass
    command = input()
hg