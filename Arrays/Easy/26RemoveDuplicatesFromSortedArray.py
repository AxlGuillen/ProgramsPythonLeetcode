def removeDuplicates(nums):
    """
    Elimina duplicados de una lista ordenada `nums` in situ y devuelve la nueva longitud de la lista sin duplicados.

    Este método recorre la lista y, cuando encuentra un valor diferente al anterior, lo mueve al inicio de la lista.
    De esta forma, mantiene el orden original de los elementos no duplicados y utiliza un contador para
    seguir la posición donde insertar el próximo valor único.

    Parámetros:
    - nums: Lista de enteros ordenada.

    Devuelve:
    - La longitud de la lista después de eliminar los duplicados.

    Además, modifica la lista `nums` in situ para dejar solo los elementos únicos en las primeras posiciones.
    """

    replace = 1  # Inicia en 1 porque el primer elemento nunca es un duplicado

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[replace] = nums[i]
            replace += 1

    print(nums[:replace])  # Modificado para imprimir solo la parte modificada de la lista
    return replace


def removeDuplicates2(nums):
    """
    Calcula el número de elementos únicos en una lista `nums`.

    Este método utiliza un conjunto para eliminar duplicados, aprovechando la propiedad de los conjuntos
    de almacenar solo elementos únicos. Es eficiente para obtener la cantidad de elementos únicos,
    pero no modifica la lista original ni mantiene el orden de los elementos.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El número de elementos únicos en la lista.
    """
    noDuplicados = set(nums)
    return len(noDuplicados)


# Uso de las funciones con ejemplo dado
nums = [1, 2, 2, 3, 3, 4, 5, 5, 5]

print("Longitud después de removeDuplicates:", removeDuplicates(nums))
# Es necesario resetear nums para la comparación justa, ya que removeDuplicates modifica nums in situ
nums = [1, 2, 2, 3, 3, 4, 5, 5, 5]
print("Cantidad de elementos únicos con removeDuplicates2:", removeDuplicates2(nums))
