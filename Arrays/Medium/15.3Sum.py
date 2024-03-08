def threeSumNotOptimized(nums):
    """
    Encuentra todas las tripletas únicas en la lista de números que sumen cero.

    Args:
        nums (list): Lista de números enteros.

    Returns:
        list: Lista de tripletas únicas que suman cero.
    """
    trios = []
    sublist = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sublist.append(nums[i])
                    sublist.append(nums[j])
                    sublist.append(nums[k])
                    sublist.sort()
                    if sublist not in trios:
                        trios.append(sublist)
                    sublist = []

    return trios


def threeSumWithSetNotOptimized(nums):
    """
    Encuentra todas las tripletas únicas en la lista de números que sumen cero.
    Utiliza un conjunto para evitar duplicados.

    Args:
        nums (list): Lista de números enteros.

    Returns:
        list: Lista de tripletas únicas que suman cero.
    """
    trios = set()
    nums.sort()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    trios.add((nums[i], nums[j], nums[k]))

    return [list(trio) for trio in trios]


def threeSumInSixthSteps(nums):
    """
    Encuentra todas las tripletas únicas en la lista de números que sumen cero
    utilizando un enfoque en seis pasos.

    Args:
        nums (list): Lista de números enteros.

    Returns:
        set: Conjunto de tripletas únicas que suman cero.
    """
    res = set()

    # Paso 1: Separa los números en positivos, negativos y ceros
    n = []
    p = []
    z = []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # Paso 2: Crea sets de los positivos y negativos para evitar duplicados
    N = set(n)
    P = set(p)

    # Paso 3: Verifica si hay ceros y crea las tripletas correspondientes
    if z:
        for num in P:
            if -1 * num in N:
                res.add((-1 * num, 0, num))

    # Paso 4: Verifica si hay tripletas de ceros
    if len(z) >= 3:
        res.add((0, 0, 0))

    # Paso 5: Verifica las duplas de números negativos para encontrar sumas que den cero
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # Paso 6: Verifica las duplas de números positivos para encontrar sumas que den cero
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res


def threeSumWithBinarySearch(nums):
    """
    Encuentra todas las tripletas únicas en la lista de números que sumen cero
    utilizando búsqueda binaria.

    Args:
        nums (list): Lista de números enteros.

    Returns:
        list: Lista de tripletas únicas que suman cero.
    """
    res = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))

                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                l += 1
                r -= 1

    return res


nums = [-1, 0, 1, 2, -1, -4]

print(threeSumNotOptimized(nums))
print(threeSumWithSetNotOptimized(nums))
print(threeSumInSixthSteps(nums))
print(threeSumWithBinarySearch(nums))


