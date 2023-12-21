def removeDuplicates(nums):
    replace = 1

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[replace] = nums[i]
            replace += 1

    print(nums)
    return replace

def removeDuplicates2(nums):

    noDuplicados = set(nums)
    return len(noDuplicados)

nums = [1,2,2,3,3,4,5,5,5]

print(removeDuplicates(nums))
print(removeDuplicates2(nums))