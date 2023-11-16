def count_specific_num(x, y):
    count = 0
    if x > y:
        return -1
    lis = [2, 3, 5, 6, 7, 8, 0]
    for i in range(x, y):
        i = str(i)
        if (
            "2" in i
            or "3" in i
            or "5" in i
            or "6" in i
            or "7" in i
            or "8" in i
            or "0" in i
        ):
            count += 1
    return 100 - count


print(count_specific_num(100, 200))
