string = input()
res = {}

for ch in string:
    if ch not in res:
        res[ch] = 0
    res[ch] += 1

res = sorted(res.items(), key=lambda x: x[0])

for alphabet, count in res:
    print(f"{alphabet}: {count} time/s")



# from collections import Counter
# string = input()
#
# res = dict(Counter(string))
#
# res = sorted(res.items(), key=lambda x: x[0])
#
# for alphabet, count in res:
#     print(f"{alphabet}: {count} time/s")
