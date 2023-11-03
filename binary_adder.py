def binary_add(one, two):
    if one > two:
        maxx = one
        max_len = len(two)
    else:
        maxx = two
        max_len = len(one)
    carry = 0
    sum = ""
    for i in range(1, max_len + 1):
        val = int(one[-i]) + int(two[-i]) + carry
        if val == 0:
            sum = "0" + sum
            carry = 0
        elif val == 1:
            sum = "1" + sum
            carry = 0
        elif val == 2:
            sum = "0" + sum
            carry = 1
        elif val == 3:
            sum = "1" + sum
            carry = 1
    i += 1

    while carry == 1 and i <= len(maxx):
        val = int(maxx[-i]) + carry
        if val == 0:
            sum = "0" + sum
            carry = 0
        elif val == 1:
            sum = "1" + sum
            carry = 0
        elif val == 2:
            sum = "0" + sum
            carry = 1
        elif val == 3:
            sum = "1" + sum
            carry = 1
        i += 1
    if carry == 1:
        return "1" + sum
    if carry == 0:
        sum = maxx[:i] + sum

    return sum


print(binary_add("110", "11"))
