def maxArea(height):
    """
    Calcula el área máxima de agua que puede ser contenida entre dos líneas, representadas por sus alturas.

    Este método implementa un algoritmo de dos punteros que comienza desde los extremos del arreglo `height` y se mueve hacia el centro. En cada paso, el algoritmo calcula el área formada entre los dos punteros y actualiza el área máxima encontrada. Luego, mueve el puntero del lado de la línea más corta hacia el interior, en busca de una línea más alta que pueda formar un contenedor con mayor capacidad.

    Parámetros:
    - height: Lista de enteros que representan las alturas de las líneas.

    Devuelve:
    - Un entero que representa el área máxima de agua contenida.
    """
    izquierda = 0
    derecha = len(height) - 1
    maxArea = 0

    while izquierda != derecha:
        largo = derecha - izquierda
        alto = min(height[izquierda], height[derecha])
        area = largo * alto
        maxArea = max(maxArea, area)
        if height[izquierda] <= height[derecha]:
            izquierda += 1
        else:
            derecha -= 1

    return maxArea


def maxAreaOptimizedMemory(height):
    """
    Versión optimizada en memoria de `maxArea`, elimina la necesidad de la función min() para calcular el alto.

    Esta función sigue un enfoque similar al de `maxArea` pero decide directamente cuál puntero mover sin calcular explícitamente el mínimo entre las alturas de los dos punteros en cada paso. Esto reduce la sobrecarga de llamadas a funciones.

    Parámetros:
    - height: Lista de enteros que representan las alturas de las líneas.

    Devuelve:
    - Un entero que representa el área máxima de agua contenida.
    """
    izquierda = 0
    derecha = len(height) - 1
    maxArea = 0

    while izquierda != derecha:
        largo = derecha - izquierda

        if height[izquierda] <= height[derecha]:
            alto = height[izquierda]
            izquierda += 1
        else:
            alto = height[derecha]
            derecha -= 1

        area = largo * alto
        maxArea = max(maxArea, area)

    return maxArea


def maxAreaOptimized(height):
    """
    Versión completamente optimizada de `maxArea` que no utiliza las funciones max() ni min().

    Este método optimiza aún más el cálculo del área máxima al evitar completamente el uso de funciones max() y min(), realizando comparaciones directas y cálculos de área en el cuerpo del bucle.

    Parámetros:
    - height: Lista de enteros que representan las alturas de las líneas.

    Devuelve:
    - Un entero que representa el área máxima de agua contenida.
    """
    capacidad_max, izquierda, derecha = 0, 0, len(height) - 1
    while izquierda < derecha:
        if height[izquierda] <= height[derecha]:
            res = height[izquierda] * (derecha - izquierda)
            izquierda += 1
        else:
            res = height[derecha] * (derecha - izquierda)
            derecha -= 1
        if res > capacidad_max:
            capacidad_max = res
    return capacidad_max


# Ejemplo de uso
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
