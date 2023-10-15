def binary_string(value):
    # 1C1B01A1
    if len(value) == 1:
        return value
    for i, j in enumerate(value):
        if j == "C" or j == "c":
            val = int(value[i - 1]) ^ int(value[i + 1])
            return binary_string(str(val) + value[i + 2 :])
        elif j == "B" or j == "b":
            val = int(value[i - 1]) or int(value[i + 1])
            return binary_string(str(val) + value[i + 2 :])
        elif j == "A" or j == "a":
            val = int(value[i - 1]) and int(value[i + 1])
            return binary_string(str(val) + value[i + 2 :])


print(binary_string("1C0C1C1A0B1"))
