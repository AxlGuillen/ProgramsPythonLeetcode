def twoSum(nums, target):
    """
    Encuentra dos números dentro de la lista `nums` que sumen `target`.

    Este método utiliza un enfoque de fuerza bruta, comparando cada par de números
    para encontrar aquellos que sumen el valor objetivo.

    Parámetros:
    - nums: Lista de enteros.
    - target: Entero que representa la suma objetivo.

    Imprime el índice de los dos números que suman `target` si se encuentran,
    de lo contrario imprime un mensaje indicando que no se encontró la suma.
    """

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

    if not encontrado:
        print('No fue encontrada la suma')


def OptimizedTwoSum(nums, target):
    """
    Encuentra dos números dentro de la lista `nums` que sumen `target`.

    Este método utiliza un enfoque optimizado, guardando previamente los números
    visitados y sus índices en un diccionario para encontrar la pareja buscada
    en tiempo lineal.

    Parámetros:
    - nums: Lista de enteros.
    - target: Entero que representa la suma objetivo.

    Imprime el índice de los dos números que suman `target` si se encuentran.
    No devuelve nada explícitamente.
    """

    prevMap = {}  # para almacenar valor e índice
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            print([prevMap[diff], i])
            return  # Añadido para terminar la función una vez se encuentre la pareja
        prevMap[n] = i


# Uso de la función con ejemplo dado
numeros = [3, 2, 4]
OptimizedTwoSum(numeros, 6)

