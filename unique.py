# n = 3

# # for i in range(n):
# #     for j in range(i + 1):
# #         print("*", end="")
# #     print()
# #     print()
# for i in range(n - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
#     print()
# 1* 2 * 3* 4* 5
# 1   2  6  24  120

num = int(input())
sum = 2
for i in range(3, num + 1):
    val = sum
    sum = 0
    for j in range(i):
        sum += val
print(sum)


# print(sum)
