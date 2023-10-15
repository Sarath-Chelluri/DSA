def diff_of_sum(m, n):
    k, l = 0, 0
    for i in range(m + 1):
        if i % n == 0:
            l += i
        else:
            k += i
    return k - l


print(diff_of_sum(10, 3))
