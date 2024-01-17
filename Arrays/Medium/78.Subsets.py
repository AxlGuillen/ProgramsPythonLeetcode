def subsets(nums):
    ans = [[]]
    if len(nums) > 2:
        ans.append(nums)
    sublist = []

    for i in range(len(nums)):
        sublist.append(nums[i])
        ans.append(sublist)
        sublist = []
        index = i + 1
        while index < len(nums):
            sublist.append(nums[i])
            sublist.append(nums[index])
            ans.append(sublist)
            sublist = []
            index += 1



    return ans



nums = [3,2,4,1,7]
ans = []

for i in range(len(nums)):
    index = 0
    sub = []
    while index <= i:
        sub.append(nums[index])
        index += 1

    ans.append(sub)


print(ans)

subsets(nums)