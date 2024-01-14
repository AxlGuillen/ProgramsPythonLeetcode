def threeSumNotOptimized(nums):
    trios = []
    sublist = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    sublist.append(nums[i])
                    sublist.append(nums[j])
                    sublist.append(nums[k])
                    sublist.sort()
                    if sublist not in trios:
                        trios.append(sublist)
                    sublist = []

    return trios

def threeSumWithSetNotOptimized(nums):
    trios = set()
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    trios.add((nums[i], nums[j], nums[k]))

    return [list(trio) for trio in trios]




    return trios



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))