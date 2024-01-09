#My version
def twoSum(nums, target):

    largo = len(nums)
    con1 = 0
    con2 = 1
    encontrado = False

    while con1 <= largo - 2:
        if con2 < largo:
            suma = nums[con1] + nums[con2]
            if suma == target:
                resultado = [con1, con2]
                print(resultado)
                encontrado = True
                break
            elif con2 < largo:
                con2 += 1
        elif con2 == largo:
            con1 += 1
            con2 = con1 + 1

    if encontrado == False:
        print('No fue encontrada la suma')

#Optimized version
def OptimizedTwoSum(nums, target):
    prevMap = {}  # para almacenar valor e índice
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            print([prevMap[diff], i])
        prevMap[n] = i
    return

numeros = [3,2,4]
OptimizedTwoSum(numeros, 6)
