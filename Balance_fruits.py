def balance_fruits(a, m, rs):
    if a > m:
        return rs - (a - m)
    elif m < a:
        return rs + (m - a)
    return rs


print(balance_fruits(14, 14, 6))
