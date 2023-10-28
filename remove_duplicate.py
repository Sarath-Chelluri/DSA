def remove_dupli(nums):
    # c = 1
    # count = 0
    # for i, j in enumerate(nums):
    #     if j == "_":
    #         continue
    #     for x in range(i + 1, len(nums)):
    #         if nums[x] > j:
    #             break
    #         if nums[x] == nums[i]:
    #             count += 1
    #             nums[x] = "_"
    # lol = count
    # for i in range(len(nums)):
    #     if lol == 0:
    #         break
    #     if nums[i] == "_":
    #         lol -= 1
    #         while nums[-c] == "_":
    #             c += 1
    #             lol -= 1
    #         nums[i], nums[-c] = nums[-c], nums[i]
    #         c += 1
    # print(nums)
    # return len(nums) - count
    count = 0
    for i, j in enumerate(nums):
        if j == "_":
            continue
        while j in nums[i + 1 :]:
            nums.remove(j)
            nums.append("_")
            count += 1
    # print(nums)
    # return len(nums) - count
    l = 0
    r = l + 1
    while r <= len(nums):
        l += 1
        n, m = nums[l], nums[r]
        while nums[l] <= nums[r]:
            n, m = nums[l], nums[r]
            r += 1
        nums[l], nums[r] = nums[r], nums[l]
        print(nums)


print(
    remove_dupli([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
)
# [0, 1, 2, 3, 4, _, _, _, _, _]
