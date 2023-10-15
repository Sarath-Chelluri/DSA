def excel(name):
    if len(name) == 1:
        print(ord(name) - 64)
        return
    print((ord(name[0]) - 64) * 26 + ord(name[1]) - 64)
    return


excel("ZZ")
