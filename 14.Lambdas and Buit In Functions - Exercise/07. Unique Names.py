def is_valid(st):
    if st[0].isupper() and all(map(lambda x: x.islower(), st[1:])):
        return st


names = input().split()

valid_names = filter(is_valid, names)
result = sum([len(name) for name in valid_names])
print(result)
