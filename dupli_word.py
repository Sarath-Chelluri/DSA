# def num_word(num):
#     nums = map(int, num)
#     return chr(sum(nums) + 64)


# print(num_word("123"))

l = [1, 2, 0, 4, 0, 5]
n = len(l)
for i in range(len(l)):
    if l[i - 1] == 0:
        continue
    if l[i] == 0:
        l.insert(i, 0)
print(l[:n])
