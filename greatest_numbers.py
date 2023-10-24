def greatest_number(arr, num):
    arr = sorted(arr)
    res = []
    for i in range(1, num + 1):
        res.append(arr[-i])
    return res


print(greatest_number([2, 4, 5, 3, 6, 8, 11, 9, 90], 2))
