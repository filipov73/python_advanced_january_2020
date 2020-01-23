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



# from collections import deque
#
#
# def crossroad():
#     global queue, green_time, safe_time, passed_cars, crash
#     green_time_left = green_time
#     safe_time_left = safe_time
#     queue = deque(queue)
#
#     while green_time_left > 0 and queue:
#         car_in_crosssection = queue.popleft()
#         car_queue = deque(car_in_crosssection)
#         while car_queue:
#             char = car_queue.popleft()
#             green_time_left -= 1
#             if green_time_left < 0:
#                 safe_time_left -= 1
#                 if safe_time_left < 0:
#                     crash = True
#                     print("A crash happened!")
#                     print(f"{car_in_crosssection} was hit at {char}.")
#                     exit()
#         passed_cars.append(car_in_crosssection)
#
#
# green_time = int(input())
# safe_time = int(input())
# queue = []
# passed_cars = []
# crash = False
#
# while True:
#     car = input()
#
#     if car == "END":
#         break
#     elif car == "green":
#         crossroad()
#     else:
#         queue.append(car)
#
# if not crash:
#     print("Everyone is safe.")
#     print(f"{len(passed_cars)} total cars passed the crossroads.")
