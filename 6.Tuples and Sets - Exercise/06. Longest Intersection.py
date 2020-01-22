def make_two_sets():
    range_ = input().split("-")
    first_start, first_end = range_[0].split(",")
    second_start, second_end = range_[1].split(",")
    set_1 = set(x for x in range(int(first_start), int(first_end) + 1))
    set_2 = set(x for x in range(int(second_start), int(second_end) + 1))
    intersection = set_1 & set_2
    # length_longest_intersection = len(intersection)
    return intersection


num = int(input())

max_len_intersection_set = set()

for _ in range(num):
    intersection_set = make_two_sets()
    len_set = len(intersection_set)
    if len(max_len_intersection_set) < len_set:
        max_len_intersection_set = intersection_set


print(f"Longest intersection is [{', '.join(str(x) for x in max_len_intersection_set)}] with length {len(max_len_intersection_set)}")