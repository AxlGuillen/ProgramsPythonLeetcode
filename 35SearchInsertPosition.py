def searchInsert(nums, target):

    if target in nums:
        for i,num in enumerate(nums):
            if num == target:
                return i
    else:
        for i in range(len(nums)-1):
            if nums[i] < target and target < nums[i+1]:
                return i + 1
        if target < nums[0]:
            return 0
        else:
            return len(nums)

#https://www.youtube.com/watch?v=K-RYzDZkzCI&ab_channel=NeetCode
def searchInsert2(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return l


nums = [1,3,4,6,7,9]
print(searchInsert(nums, 10))
print(searchInsert2(nums, 10))