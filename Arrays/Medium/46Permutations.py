"""
Este script define una función 'permute' que genera todas las permutaciones posibles
de una lista de números. Utiliza un enfoque de backtracking para explorar todas las
combinaciones posibles, colocando cada número en cada posición posible una vez por permutación.

La función 'solve' es una función auxiliar recursiva utilizada por 'permute' para construir
las permutaciones. 'solve' toma la lista original de números, una plantilla de permutación
actual (inicialmente marcada con 11s para indicar posiciones no asignadas) y un contador 'c'
que rastrea la profundidad de la recursión y la posición del número actual a insertar en la permutación.

Las permutaciones completas se añaden a una lista 'ans', que es devuelta al finalizar la ejecución de 'permute'.
"""

def permute(nums):
    # Función auxiliar para generar permutaciones.
    def solve(nums, per, c):
        # Si 'c' es igual al tamaño de 'nums', hemos encontrado una permutación completa.
        if c == len(nums):
            # Añade una copia de la permutación actual a la lista de respuestas.
            ans.append(list(per))
            return
        # Itera sobre todos los elementos posibles para encontrar permutaciones.
        for i in range(len(nums)):
            # Verifica si la posición actual en 'per' está disponible (marcado por el valor 11).
            if per[i] == 11:
                # Asigna el valor actual de 'nums' a la permutación y continua explorando.
                per[i] = nums[c]
                solve(nums, per, c + 1)
                # Restaura el valor anterior para permitir nuevas combinaciones.
                per[i] = 11

    # Inicializa la lista para almacenar todas las permutaciones encontradas.
    ans = []
    # Inicializa la plantilla de permutación con todos los valores establecidos en 11 (indicador de posición no utilizada).
    per = [11] * len(nums)
    # Comienza el proceso de generación de permutaciones.
    solve(nums, per, 0)
    # Retorna la lista de permutaciones generadas.
    return ans

# Lista de números para generar permutaciones.
nums = [1,2,3,4]
# Imprime las permutaciones generadas para la lista de números dada.
print(permute(nums))