def sortMatrix(mat):
    lis = []
    for i in mat:
        for j in i:
            lis.append(j)
    lis = sorted(lis)
    c = 0
    matt = []
    for i in range(len(mat)):
        l = []
        for j in range(len(mat[i])):
            l.append(lis[c])
            c += 1
        matt.append(l)

    print(matt)


sortMatrix([[2, 4, 7, 5, 3], [6, 4, 2, 6, 7], [8, 9, 21, 1, 2]])
