start = int(input())
end = int(input())
numbers = [num for num in range(start, end + 1)]
numbers_one_to_ten = [num for num in range(2, 11)]
filtered = [num for num in numbers if any([num % x == 0 for x in numbers_one_to_ten])]
print(filtered)



# def is_valid(number):
#     min_number = 2
#     max_number = 10
#     results = [x for x in range(min_number, max_number + 1) if number % x == 0]
#     return True if results else False
#
#
# n = int(input())
# m = int(input())
#
# result = [x for x in range(n, m + 1) if is_valid(x)]
# print(result)
