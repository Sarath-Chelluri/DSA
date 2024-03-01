# import math


# def Matrix_encode(words):
#     x = len(words) ** 0.5
#     l = math.floor(x)
#     h = math.ceil(x)
#     mat = []
#     y = 0
#     if l * h > len(words):
#         l = h
#     for i in range(l):
#         tem = []
#         for j in range(h):
#             if y >= len(words):
#                 tem.append(" ")
#                 y += 1
#                 continue
#             tem.append(words[y])
#             y += 1
#         mat.append(tem)
#     for i in range(l):
#         for j in range(h):
#             print(mat[j][i], end="")


# Matrix_encode("stringargs")

# take a 3x3 matrix
A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

# result will be 3x4
print(*B)
result = [
    [sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A
]

for r in result:
    print(r)
