def autobio(num):
    if num == "":
        return None
    sett = set()
    for i, k in enumerate(num):
        count = 0
        sett.add(k)
        for j in num:
            if str(i) == j:
                count += 1
        if str(count) != num[i]:
            return 0
    return len(sett)


print(autobio("1210"))
