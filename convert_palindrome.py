def palindrome(num):
    if num == num[::-1]:
        return num
    return num + num[:-1:][::-1]


print(palindrome("abcd"))
