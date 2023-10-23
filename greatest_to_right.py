arr1 = list(map(int, input().split()))


def find_greatest_to_right(arr, n):
    # count = 0
    # for i in range(n):
    #     small = False
    #     for j in range(i, n):
    #         if arr[i] < arr[j]:
    #             small = True
    #             break
    #     if not small:
    #         count += 1
    # return count
    count = 0
    for i in range(n - 1):
        rest = arr[i + 1 :]
        if max(rest) < arr[i]:
            count += 1
    return count + 1


print(find_greatest_to_right(arr1, len(arr1)))
