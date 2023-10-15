def sumoddeven(arr):
    eve = []
    odd = []
    for i, j in enumerate(arr):
        if i % 2 == 0:
            eve.append(j)
        else:
            odd.append(j)
    maxx = sorted(eve, reverse=True)[1]
    minn = sorted(odd)[1]
    return maxx + minn


print(sumoddeven([1, 8, 0, 2, 3, 5, 6]))
