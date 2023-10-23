def fac(num):
    count = 0
    for i in range(1, num + 1):
        for j in range(1, num // 2):
            if i != j and i * j == num:
                count += 1
                break
    return count


print(fac(18))
