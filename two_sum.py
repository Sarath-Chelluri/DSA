def two_summ(arr, val):
    sett = {}
    for i, j in enumerate(arr):
        if j in sett:
            return [sett[j] + 1, i + 1]
        else:
            sett[val - j] = i
    return []


print(
    two_summ(
        [2, 3, 4, 7],
        9,
    )
)
