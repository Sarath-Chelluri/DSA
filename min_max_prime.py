def min_max_primee(arr):
    max_prime = 0
    min_prime = float("inf")
    print(max_prime)
    for i in arr:
        if is_prime(i):
            min_prime = min(min_prime, i)
            max_prime = max(max_prime, i)
    return min_prime, max_prime


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


print(min_max_primee([97, 3, 6, 34, 17, 45, 4]))
