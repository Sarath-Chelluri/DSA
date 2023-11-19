def uniqueChar(string):
    l = []
    check = ""
    for i in string:
        if i not in check:
            l.append(i)
            check += i
    for i in l:
        print(i, end=" ")


uniqueChar("hello maninn inso i")
