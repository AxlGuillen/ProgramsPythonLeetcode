def searchInsert(nums, target):
    """
    Busca la posición de inserción de `target` en una lista ordenada `nums`.

    Si `target` ya existe en `nums`, devuelve su índice. Si no, devuelve el índice donde `target`
    debería ser insertado para mantener el orden de la lista.

    Este método utiliza una búsqueda lineal, lo que lo hace menos eficiente para listas grandes.

    Parámetros:
    - nums: Lista de enteros ordenada.
    - target: Entero a buscar o insertar.

    Devuelve:
    - Índice en el que `target` está o debería estar en `nums`.

    Ejemplo de uso:
    >>> searchInsert([1,3,5,6], 5)
    2
    >>> searchInsert([1,3,5,6], 2)
    1
    """

    if target in nums:
        for i, num in enumerate(nums):
            if num == target:
                return i
    else:
        for i in range(len(nums) - 1):
            if nums[i] < target < nums[i + 1]:
                return i + 1
        if target < nums[0]:
            return 0
        else:
            return len(nums)


# Referencia al video de YouTube para una explicación adicional del algoritmo
# https://www.youtube.com/watch?v=K-RYzDZkzCI&ab_channel=NeetCode

def searchInsert2(nums, target):
    """
    Busca la posición de inserción de `target` en una lista ordenada `nums` utilizando búsqueda binaria.

    Este método es más eficiente que `searchInsert`, especialmente para listas grandes, ya que reduce
    el tiempo de búsqueda dividiendo repetidamente a la mitad el rango de búsqueda.

    Parámetros:
    - nums: Lista de enteros ordenada.
    - target: Entero a buscar o insertar.

    Devuelve:
    - Índice en el que `target` está o debería estar en `nums`.

    Ejemplo de uso:
    >>> searchInsert2([1,3,5,6], 5)
    2
    >>> searchInsert2([1,3,5,6], 2)
    1
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return l


nums = [1, 3, 4, 6, 7, 9]
print(searchInsert(nums, 10))  # Esperado: 6
print(searchInsert2(nums, 10))  # Esperado: 6
