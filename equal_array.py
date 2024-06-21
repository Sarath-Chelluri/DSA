def equalize(array):
    count = 0
    while not same_elements(array):
        index = array.index(max(array))
        array = increment_but_1(array, index)
        count += 1
    return count


def same_elements(array):
    a = array[0]
    for i in array:
        if a != i:
            return False
    return True


def increment_but_1(array, index):
    for i in range(len(array)):
        if i == index:
            continue
        array[i] += 1
    return array


print(equalize([3, 4, 4]))
