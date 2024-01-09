def search(nums, target):

    left = 0
    right = len(nums) - 1
    m = (left + right) // 2

    if target in nums:
        while nums[m] != target:
            if nums[m] < target:
                left = m + 1
            else:
                right = m - 1
            m = (left + right) // 2
        return m

    return -1


nums = [-1, 0, 3, 5, 9, 12]
print(search(nums,12))