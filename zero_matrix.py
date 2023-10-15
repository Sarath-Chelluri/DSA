# insert zeros for all the rows and columns if the element is zero
# [123] [103]
# [103] [000]
# [123] [103]
li = []
mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def check_zero(m, n):
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                li.append([i, j])


def zeroify(i, j):
    x = y = 0
    while len(mat) > x:
        mat[x][j] = 0
        x += 1
    while len(mat[0]) > y:
        mat[i][y] = 0
        y += 1
    print(mat)


check_zero(3, 4)
print(li)
for i in li:
    zeroify(i[0], i[1])
