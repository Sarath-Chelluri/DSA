def max_subset(nums, lenn):
    sub_sum = nums[0]
    for i in range(1, lenn):
        if sub_sum < 0:
            i += 1
            sub_sum = 0
            sub_set = nums[i:]
        sub_sum += nums[i]

    print(sub_set, sub_sum)


max_subset([-2, 1, -3, 4, -1, 2, 1, -5, 4], 9)
