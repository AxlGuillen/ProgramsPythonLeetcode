def majorityElement(nums):
    numeros = {}
    existentes = list(set(nums))
    for num in existentes:
        numeros[num] = 0
    for num in nums:
        numeros[num] +=1
    valor2 = max(numeros.values())

    for clave, valor in numeros.items():
        if valor2 == valor:
            return clave

def majorityElement2(nums):
    existentes = set(nums)

    for num in existentes:
        contador = nums.count(num)
        if contador > len(nums) // 2:
            return num

#Best in memory
def majorityElementOneLine(nums):
    return sorted(nums)[len(nums) // 2]


nums = [2,2,1,1,1,2,2,3]
print(majorityElementOneLine(nums))