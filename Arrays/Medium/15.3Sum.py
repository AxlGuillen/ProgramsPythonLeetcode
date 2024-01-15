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

def threeSumInSixthSteps(nums):

    res = set()

    #1.-Separa los numeros en positivos negativos y zeros
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

    #2.-Crea 2 set de los positivos y negativos para que no se repitan
    N = set(n)
    P = set(p)

    #3.-Revisa si hay 0 y empieza a hacer las duplas (1, -1)(2, -2)
    #   para asi saber si el complemento que necesita existe
    if z:
        for num in P:
            if -1 * num in N:
                res.add((-1 * num, 0, num))

    #4.- Verifica si existe la opcion de un triple 0
    if len(z) >= 3:
        res.add((0, 0, 0))

    #5.- Verifica cada dupla de numeros negativos y revisa si hay su suma en positivo para que de 0
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    #6.- Para toda dupla de numeros positivos verifica si existe su suma en negativo para que de 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res

def threeSumWithBinarySearch(nums):
    # Inicializa una lista para almacenar los tríos que suman cero
    res = []

    # Ordena la lista para facilitar la búsqueda de tríos y evitar duplicados
    nums.sort()

    # Itera a través de cada número, excepto los últimos dos
    for i in range(len(nums) - 2):
        # Evita tríos repetidos saltando números iguales al anterior
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Inicializa dos punteros, uno a la derecha del número actual y otro al final
        l, r = i + 1, len(nums) - 1

        # Mientras el puntero izquierdo sea menor que el derecho
        while l < r:
            # Calcula la suma del trío actual
            s = nums[i] + nums[l] + nums[r]

            # Si la suma es menor que cero, mueve el puntero izquierdo hacia la derecha
            if s < 0:
                l += 1
            # Si la suma es mayor que cero, mueve el puntero derecho hacia la izquierda
            elif s > 0:
                r -= 1
            # Si la suma es cero, se encontró un trío válido
            else:
                # Añade el trío a la lista de resultados
                res.append((nums[i], nums[l], nums[r]))

                # Mueve el puntero izquierdo mientras el siguiente número sea igual
                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                # Mueve el puntero derecho mientras el anterior número sea igual
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1

                # Mueve ambos punteros hacia el centro
                l += 1
                r -= 1

    # Retorna la lista de tríos únicos que suman cero
    return res



nums = [-1,0,1,2,-1,-4]

print(threeSumNotOptimized(nums))
print(threeSumWithSetNotOptimized(nums))
print(threeSumInSixthSteps(nums))
print(threeSumWithBinarySearch(nums))

