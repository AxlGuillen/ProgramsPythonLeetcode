def singleNumber(nums):

    while len(nums) > 1:
        par_encontrado = False
        numero = nums[0]
        for i in range(1, len(nums)):
            if numero == nums[i]:
                nums.pop(i)
                nums.pop(0)
                par_encontrado = True
                break
        if not par_encontrado:
            break

    return nums[0]
def singleNumberNotOptimized(nums):

    registrados=[]

    for indice in range(len(nums)):
        i = indice+1
        while i < len(nums):
            if nums[indice] in registrados:
                break
            elif nums[indice] == nums[i]:
                registrados.append(nums[indice])
            i+=1
        if nums[indice] not in registrados:
            return nums[indice]
def singleNumberOptimized(nums):
    return sum(list(set(nums)))*2 - sum(nums)


nums=[1,2,5,5,1]
print(singleNumber(nums))