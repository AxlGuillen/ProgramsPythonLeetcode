def moveZeroesAnaVersionBestMemory(nums):

    for i in range(nums.count(0)):
        #remove quita el primero que encuentra
        nums.remove(0)
        nums.append(0)

    return nums

def moveZeroesBestRunTime(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

def moveZeroesWithList(nums):

    sinCeros = []
    conCeros = []

    for n in nums:
        if n == 0:
            conCeros.append(n)
            continue
        sinCeros.append(n)


    return sinCeros + conCeros

def moveZeroes(nums):

    for i in range(len(nums)-1):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break

    return nums

nums = [0,1,0,3,12]

print(moveZeroesAnaVersionBestMemory(nums))
print(moveZeroesBestRunTime(nums))
print(moveZeroesWithList(nums))
print(moveZeroes(nums))

