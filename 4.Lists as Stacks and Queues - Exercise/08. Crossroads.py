from collections import deque
green_light = int(input())
free_window = int(input())

car = input()
crash = False
temp_sec = 0
counter = 0
cars_deque = deque()
while car != "END":
    if car == "green":
        temp_sec = green_light
        while cars_deque:
            temp_sec -= len(cars_deque[0])
            if temp_sec > 0:
                cars_deque.popleft()
                counter += 1
            else:
                temp_sec += free_window
                if temp_sec > len(cars_deque[0]):
                    cars_deque.popleft()
                    counter += 1
                    break
                else:
                    crash_part = cars_deque[0][temp_sec]
                    print("A crash happened!")
                    print(f"{cars_deque[0]} was hit at {crash_part}.")
                    crash = True
                    break
        if crash:
            break
    else:
        cars_deque.append(car)
    car = input()

if not crash:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")