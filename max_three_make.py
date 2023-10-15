def maxer(num1, num2, num3):
    new = ""
    for i, j in enumerate(str(num1)):
        new += str(max(int(str(num1)[i]), int(str(num2)[i]), int(str(num3)[i])))
    return int(new)


print(maxer(3521, 2452, 1352))
