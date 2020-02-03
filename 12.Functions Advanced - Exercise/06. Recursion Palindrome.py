
def palindrome(string, idx):
    end_idx = len(string) - idx - 1
    if idx > end_idx:
        return f'{string} is a palindrome'
    if string[idx] == string[end_idx]:
        return palindrome(string, idx + 1)

    else:
        return f"{string} is not a palindrome"



print(palindrome("abcba", 0))
print(palindrome("peter", 0))
