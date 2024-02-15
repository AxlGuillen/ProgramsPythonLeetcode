def generate(numRows):
    """
    Genera el triángulo de Pascal hasta un número especificado de filas.

    Cada fila del triángulo de Pascal tiene un número más que la fila anterior,
    comenzando con una sola entrada en la parte superior. El primer y último número
    de cada fila es siempre 1, y cada número entre ellos es la suma de los dos números
    directamente arriba de él en la fila anterior.

    Parámetros:
    - numRows: Un entero que especifica el número de filas del triángulo de Pascal a generar.

    Devuelve:
    - Una lista de listas, donde cada sublista representa una fila del triángulo de Pascal.

    Ejemplo de uso:
    >>> generate(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    piramide = []

    for i in range(numRows):
        nivel = []
        for j in range(i + 1):
            if j == 0 or j == i:
                nivel.append(1)
            else:
                numero = piramide[i - 1][j - 1] + piramide[i - 1][j]
                nivel.append(numero)
        piramide.append(nivel)

    return piramide


def generate2(numRows):
    """
    Una variante de la función `generate` que también genera el triángulo de Pascal
    hasta un número especificado de filas. Esta implementación modifica directamente
    la lista de listas `piramide` durante la construcción de cada fila.

    Parámetros:
    - numRows: Un entero que especifica el número de filas del triángulo de Pascal a generar.

    Devuelve:
    - Una lista de listas, donde cada sublista representa una fila del triángulo de Pascal.

    Ejemplo de uso:
    >>> generate2(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """

    piramide = []

    for i in range(numRows):
        piramide.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                piramide[i].append(1)
            else:
                piramide[i].append(piramide[i - 1][j - 1] + piramide[i - 1][j])

    return piramide


# Ejemplo de uso
numRows = 4
print(generate2(numRows))
