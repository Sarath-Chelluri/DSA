def arrayinarray(arr1, arr2, arr3):
    x = []
    y = []
    for i in arr1:
        if i not in arr2:
            x.append(i)
    for j in arr2:
        if j not in arr3:
            y.append(j)

    return x, y


print(camelCase([1, 2, 3, 4, 5], [3, 4, 5, 6], [5, 6, 7]))
