def rotateMyVersionOutOfTheLimit(matrix):
    response = []
    for i in range(len(matrix)):          # Recorre cada columna de la matriz original
        aux = []
        for j in range(len(matrix)):      # Para cada fila en la matriz original
            aux.insert(0, matrix[j][i])   # Inserta el elemento en la posición 0 de la lista auxiliar
        response.append(aux)              # Añade la lista auxiliar a la matriz respuesta
    print(response)


def rotateInversionMethod(matrix):
    matrix = matrix[::-1]  # Invierte la matriz de arriba a abajo

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            # Intercambia el elemento [i][j] con [j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)


def rotate(matrix):
    """
    Rota la matriz 90 grados en el sentido de las agujas del reloj.
    Este método realiza dos operaciones principales:

    1. Invertir la matriz: Se usa el slicing [::-1] para invertir el orden de las filas de la matriz,
       de modo que la primera fila se convierte en la última y viceversa.

    2. Transponer la matriz: Se utiliza la función zip en combinación con el operador *,
       para desempaquetar las filas de la matriz invertida y agruparlas por columnas.

       - `*matrix[::-1]` desempaqueta cada fila de la matriz invertida como un argumento separado para zip.
       - `zip(...)` toma el primer elemento de cada fila desempaquetada (ahora argumentos separados), y los agrupa en una tupla,
         haciendo lo mismo para el segundo elemento, y así sucesivamente, resultando en nuevas tuplas que forman las columnas de la
         matriz rotada.

    Finalmente, se asigna el resultado de zip (convertido a lista) de vuelta a la matriz original usando matrix[:],
    lo que permite que la modificación sea in-place (directamente en la matriz original sin cambiar su referencia).
    """
    # Invierte la matriz y luego transpone cada columna a fila, asignando el resultado in-place
    matrix[:] = zip(*matrix[::-1])




matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMyVersionOutOfTheLimit(matrix)
rotateInversionMethod(matrix)
