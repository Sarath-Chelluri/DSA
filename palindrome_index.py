def palin_index(s):
    if s == s[::-1]:
        return -1
    for i in range(1, len(s) + 1):
        c = s[: i - 1] + s[i:]
        if c == c[::-1]:
            return i
    return -1


palin_index("sarath")
