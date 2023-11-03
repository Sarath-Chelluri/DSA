def binary_adder(a, b):
    carry = 0
    res = ""
    i = 1
    j = 1
    if len(a) > len(b):
        b = (len(a) - len(b)) * "0" + b
    else:
        a = (len(b) - len(a)) * "0" + a

    while i <= len(a):  # 3 # 0 0 0 # 1 1 1
        # print(a[-i], b[-j], carry)  # 1 1 0
        if carry:
            if int(a[-i]) & int(b[-j]):
                res = "0" + res
            else:
                res = "1" + res
                carry = 0
        elif int(a[-i]) & int(b[-j]):
            res = "0" + res  # 0
            carry = 1
        elif a[-i] == "0" and b[-j] == "0":
            res = "0" + res
        else:
            res = "1" + res
        i += 1
        j += 1

    return res


print(binary_adder("100", "101"))
