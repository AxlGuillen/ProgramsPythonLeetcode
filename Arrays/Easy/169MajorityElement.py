def majorityElement(nums):
    """
    Encuentra el elemento mayoritario en la lista `nums` utilizando un diccionario
    para contar la aparición de cada elemento. Este método primero crea un conjunto de
    elementos únicos y luego cuenta cuántas veces aparece cada uno en la lista original.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El elemento que aparece más de n/2 veces en la lista, donde n es el tamaño de la lista.
    """

    numeros = {}
    existentes = list(set(nums))
    for num in existentes:
        numeros[num] = 0
    for num in nums:
        numeros[num] += 1
    valor2 = max(numeros.values())

    for clave, valor in numeros.items():
        if valor2 == valor:
            return clave


def majorityElement2(nums):
    """
    Encuentra el elemento mayoritario en la lista `nums` de manera más directa,
    iterando sobre un conjunto de elementos únicos y contando las ocurrencias de
    cada uno en la lista original. Si un elemento se cuenta más de n/2 veces, se
    devuelve inmediatamente.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El elemento mayoritario en la lista.
    """

    existentes = set(nums)

    for num in existentes:
        contador = nums.count(num)
        if contador > len(nums) // 2:
            return num


def majorityElementOneLine(nums):
    """
    Encuentra el elemento mayoritario en la lista `nums` utilizando un enfoque altamente
    eficiente y minimalista. Al ordenar la lista, el elemento en la posición media es
    necesariamente el elemento mayoritario.

    Parámetros:
    - nums: Lista de enteros.

    Devuelve:
    - El elemento mayoritario en la lista.

    Nota: Este método es el más eficiente en términos de simplicidad del código y uso de memoria.
    """

    return sorted(nums)[len(nums) // 2]


# Ejemplo de uso
nums = [2, 2, 1, 1, 1, 2, 2, 3]
print("Elemento mayoritario (método de una línea):", majorityElementOneLine(nums))
