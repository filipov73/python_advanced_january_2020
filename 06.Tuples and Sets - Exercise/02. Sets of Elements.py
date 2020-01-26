def add_element(sets, n):
    s = sets
    for _ in range(n):
        e = input()
        s.add(e)
    return s


(n, m) = input().split(" ")
first_set = set()
second_set = set()

add_element(first_set, int(n))
add_element(second_set, int(m))
res = first_set & second_set
for el in res:
    print(el)
