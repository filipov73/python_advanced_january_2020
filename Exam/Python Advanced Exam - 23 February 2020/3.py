def get_repeating_DNA(dna):
    temp = dna.split()
    rez = []
    result = []

    while len(dna) >= 10:
        temp_rez = dna[:10]
        if all([True if x in ["A", "G", "C", "T"] else False for x in temp_rez]):
            rez.append(temp_rez)
        x = dna[1:]
        dna = x
    for x in rez:
        count = rez.count(x)
        if count > 1:
            result.append(x)
            rez.remove(x)
    return  result



test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGG CCGACTTCCA AGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

