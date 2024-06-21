def count_steps(t, arr):
    # count = 0
    # i = 0
    # while arr[-1] != 0:
    #     r = t
    #     count += 2 * i
    #     i = 0
    #     while r != 0:
    #         if arr[i] <= r:
    #             r -= arr[i]
    #             arr[i] = 0
    #             i += 1
    #         if i >= len(arr):
    #             break
    #         if arr[i] > r:
    #             break
    # return count + 6

    vol = t
    ans = 0
    for i in arr:
        x = i <= vol
        ans += (2 if x else 0) * i + 1
        vol = vol if x else t
    return ans


print(count_steps(4, [1, 1, 1, 4, 2, 3]))
