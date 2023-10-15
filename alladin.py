def alladin(num, count=-1):
    if num == 4:
        return count
    count += 1
    if num % 2 == 0:
        return alladin(num / 2, count)
    else:
        return alladin((num * 3) + 1, count)


print(alladin(6))


def count(n):
    count = -1
    while n != 4:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
        count += 1
    return count


print(count(5))
