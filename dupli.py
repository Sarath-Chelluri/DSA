# [1,1,2,3,4,5]

li = [1, 1, 1, 2, 2, 3, 7, 4, 7, 4, 5, 5, 5, 5]

for i, j in enumerate(li):
    if i == 0:
        print(j)
    if i != 0 and li[i - 1] != j:
        print(j)
    else:
        continue
