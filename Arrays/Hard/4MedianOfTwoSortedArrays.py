def findMedianSortedArrays(nums1, nums2):
    """
    Calcula la mediana de dos listas ordenadas de enteros.

    La función primero encuentra el mínimo y el máximo entre el primer elemento de `nums1` y `nums2` y el último elemento de `nums1` y `nums2`, respectivamente. Luego, calcula el promedio de los medios de cada lista y devuelve el promedio de estos dos promedios como la 'mediana', aunque este no es el cálculo correcto de la mediana para dos listas ordenadas combinadas.

    Parámetros:
    - nums1: Lista de enteros ordenada.
    - nums2: Lista de enteros ordenada.

    Devuelve:
    - Un flotante que representa la 'mediana' calculada de `nums1` y `nums2` según la lógica descrita, que no es el cálculo tradicional de la mediana.

    Nota: Este método no implementa el cálculo correcto de la mediana para dos listas ordenadas combinadas. Para un cálculo correcto, se deberían combinar ambas listas y luego encontrar la mediana de la lista resultante.
    """

    # Longitudes de las listas
    l1 = len(nums1)
    l2 = len(nums2)

    # Encuentra el mínimo y máximo entre los primeros y últimos elementos de cada lista
    menor = min(nums1[0], nums2[0])
    maximo = max(nums1[l1 - 1], nums2[l2 - 1])

    # Calcula el promedio de los medios de cada lista
    m1 = (nums1[0] + nums1[l1 - 1]) / 2
    m2 = (nums2[0] + nums2[l2 - 1]) / 2

    # Calcula el promedio de los promedios como 'mediana'
    mediana = (m1 + m2) / 2

    return mediana


# Ejemplo de uso
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
