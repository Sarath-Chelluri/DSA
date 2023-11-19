def camelCase(str):
    words = []
    strr = str
    cn = 0
    for i in range(1, len(str) - 1):
        if str[i + 1].isupper():
            words.append(strr[: i + 1 - cn])
            strr = strr[i + 1 - cn :]
            cn = len(strr[: i + 1])
    for i in words:
        print(i.swapcase())
    print(strr.swapcase())
    return


camelCase("hiHelloHamsterGoo")
