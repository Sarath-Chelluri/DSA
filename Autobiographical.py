def autobio(num):
    if num == "":
        return None

    for i, k in enumerate(num):
        count = 0
        for j in num:
            if str(i) == j:
                count += 1
        if str(count) != num[i]:
            return 0


autobio("1210")
