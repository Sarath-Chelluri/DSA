def number_bigger(num):
    if num == 1:
        return 1
    if num == 2:
        return 22
    midh = ""
    midl = ""
    for i in range(num - 2):
        midl += "0"
        midh += "9"
    vall = str(num) + midl + str(num)
    valh = str(num) + midh + str(num)

    return vall, valh


print(number_bigger(4))
