def removeElement(nums) -> int:
    count = len(nums)
    for i, j in enumerate(nums):
        if j == "_":
            continue
        for x in range(i + 1, len(nums)):
            if j not in nums[i + 1 :]:
                break
            if j == nums[x]:
                nums[x] = "_"
                count -= 1
    print(nums)
    return count


print(removeElement([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
