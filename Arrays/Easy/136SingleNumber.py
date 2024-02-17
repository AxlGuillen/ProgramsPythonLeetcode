def singleNumber(nums):
    """
    Encuentra el número que aparece exactamente una vez en la lista, donde cada otro número
    aparece exactamente dos veces. Esta implementación elimina iterativamente pares de números
    iguales hasta que solo queda el número único.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El entero que aparece exactamente una vez en la lista.

    Nota: Este enfoque no es óptimo desde el punto de vista del tiempo de ejecución, especialmente
    para listas grandes, ya que modifica la lista mientras se itera sobre ella.
    """

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
    """
    Encuentra el número que aparece exactamente una vez en la lista mediante el seguimiento
    de los números ya examinados. Si un número se encuentra por segunda vez, se agrega a una
    lista de 'registrados' para no considerarlo en futuras iteraciones.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El entero que aparece exactamente una vez en la lista.

    Nota: Aunque funcional, este enfoque es ineficiente para listas grandes debido a su
    complejidad algorítmica.
    """

    registrados = []

    for indice in range(len(nums)):
        i = indice + 1
        while i < len(nums):
            if nums[indice] in registrados:
                break
            elif nums[indice] == nums[i]:
                registrados.append(nums[indice])
            i += 1
        if nums[indice] not in registrados:
            return nums[indice]


def singleNumberOptimized(nums):
    """
    Encuentra el número único en la lista de una manera altamente optimizada.
    Utiliza la propiedad matemática de que la suma del doble de la suma de elementos únicos
    menos la suma de todos los elementos de la lista, da como resultado el elemento único.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El entero que aparece exactamente una vez en la lista.

    Nota: Este enfoque es mucho más eficiente, especialmente para listas grandes,
    ya que se basa en operaciones de suma y conjunto que son más rápidas que iterar
    y modificar listas.
    """
    return sum(list(set(nums))) * 2 - sum(nums)


# Ejemplo de uso
nums = [1, 2, 5, 5, 1]
print("Número único (método inicial):",
      singleNumber(nums.copy()))  # Se usa nums.copy() para evitar modificar la lista original
print("Número único (método optimizado):", singleNumberOptimized(nums))
