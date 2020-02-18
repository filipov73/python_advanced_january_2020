from collections import deque


def check_25(num):
    return num % 25 == 0 and num != 0


males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
counter = 0
while males and females:
    # if males[-1] <= 0:
    #     males.pop()
    #     continue
    # if females[0] <= 0:
    #     females.popleft()
    #     continue
    # if check_25(males[-1]):
    #     males.pop()
    #     males.pop()
    #     continue
    # if check_25(females[0]):
    #     females.popleft()
    #     females.popleft()
    #     continue
    # if males[-1] == females[0]:
    #     males.pop()
    #     females.popleft()
    #     counter += 1
    # else:
    #     females.popleft()
    #     males[-1] -= 2

    current_male = males.pop()
    current_female = females.popleft()
    if current_male <= 0 or current_female <= 0:
        if current_male > 0:
            males.append(current_male)
        if current_female > 0:
            females.appendleft(current_female)
        continue
    if check_25(current_female):
        females.popleft()
        males.append(current_male)
        continue
    if check_25(current_male):
        males.pop()
        females.appendleft(current_female)
        continue
    if current_male == current_female:
        counter += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {counter}")
if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")
