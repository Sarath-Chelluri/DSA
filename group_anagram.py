def group_anagrams(arr):
    lists = arr.split()
    res = []
    dic = {}
    for i, j in enumerate(lists):
        sett = set()
        for y in j:
            sett.add(y)
        dic[i] = sett
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if dic[i] == dic[j]:
                res.append([i, j])

    return res


print(group_anagrams("dog man nam dog"))
