def find_count(arr, n, diff, num):
    count = 0
    for i in arr:
        if abs(num - i) <= diff:
            count += 1
    if count == 0:
        return -1
    return count


print(find_count([12, 3, 14, 77, 91, 13], 6, 2, 13))
