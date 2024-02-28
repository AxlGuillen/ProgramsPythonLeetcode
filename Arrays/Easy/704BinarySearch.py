def search(nums, target):
    """
    Realiza una búsqueda binaria en una lista ordenada de enteros para encontrar el índice del elemento objetivo.

    La búsqueda binaria encuentra la posición de un elemento objetivo dentro de una lista ordenada comparando
    el elemento objetivo con el valor medio de la lista. Si no son iguales, la mitad en la cual el elemento
    no puede estar es eliminada y la búsqueda continúa en la mitad restante hasta que el elemento es encontrado
    o la lista se reduce a cero.

    Parámetros:
    - nums: Lista de enteros ordenada en la que se realizará la búsqueda.
    - target: El valor entero que se busca en la lista.

    Devuelve:
    - El índice del elemento objetivo dentro de la lista si se encuentra; de lo contrario, devuelve -1.

    Ejemplo de uso:
    >>> search([-1, 0, 3, 5, 9, 12], 9)
    4
    >>> search([-1, 0, 3, 5, 9, 12], 2)
    -1
    """

    left = 0
    right = len(nums) - 1

    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            left = m + 1
        else:
            right = m - 1

    return -1


# Ejemplo de uso
nums = [-1, 0, 3, 5, 9, 12]
print(search(nums, 12))  # Debería devolver 5
