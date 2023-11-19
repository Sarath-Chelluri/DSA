def nthPrime(num):
    count = 0
    val = 1
    while count != num:
        val += 1
        if is_prime(val):
            count += 1
    return val


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


print(nthPrime(11))
