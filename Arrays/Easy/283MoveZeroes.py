def moveZeroesAnaVersionBestMemory(nums):
    """
    Mueve todos los ceros al final de la lista `nums` modificando la lista in situ.
    Este método elimina los ceros uno por uno y los agrega al final de la lista.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - La misma lista con todos los ceros movidos al final.

    Nota: Este método es eficiente en términos de uso de memoria porque modifica la lista in situ,
    pero puede ser menos eficiente en tiempo de ejecución debido al coste de eliminar elementos en medio de la lista.
    """

    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

    return nums


def moveZeroesBestRunTime(nums):
    """
    Mueve todos los ceros al final de la lista `nums` de manera óptima en tiempo de ejecución,
    utilizando un enfoque de dos punteros.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - La misma lista con todos los ceros movidos al final, optimizando el tiempo de ejecución.

    Nota: Este método es el más rápido porque minimiza las operaciones de asignación, intercambiando
    ceros por elementos no cero directamente cuando los encuentra.
    """

    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums


def moveZeroesWithList(nums):
    """
    Mueve todos los ceros al final de la lista `nums` construyendo dos listas separadas:
    una para elementos no cero y otra para los ceros, y luego concatenándolas.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - Una nueva lista con todos los ceros movidos al final.

    Nota: Aunque este método es intuitivo y fácil de entender, no modifica la lista in situ y
    requiere espacio adicional para las listas temporales.
    """

    sinCeros = [n for n in nums if n != 0]
    conCeros = [n for n in nums if n == 0]

    return sinCeros + conCeros


def moveZeroes(nums):
    """
    Mueve todos los ceros al final de la lista `nums` mediante un enfoque de doble bucle,
    buscando ceros y elementos no cero para intercambiarlos hasta que todos los ceros estén al final.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - La misma lista con todos los ceros movidos al final.

    Nota: Este método puede ser ineficiente en listas grandes debido a su enfoque de doble bucle.
    """

    for i in range(len(nums) - 1):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

    return nums


# Ejemplo de uso
nums = [0, 1, 0, 3, 12]

print("AnaVersionBestMemory:", moveZeroesAnaVersionBestMemory(nums.copy()))
print("BestRunTime:", moveZeroesBestRunTime(nums.copy()))
print("WithList:", moveZeroesWithList(nums.copy()))
print("BasicMoveZeroes:", moveZeroes(nums.copy()))


