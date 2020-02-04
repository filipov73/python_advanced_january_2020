
num = int(input())
list_ = [int(x) for x in input().split()]

result = map(lambda x: x * num, list_)
print(" ".join(map(str, result)))
