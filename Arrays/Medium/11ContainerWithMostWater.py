def maxArea(height):
    izquierda = 0
    derecha = len(height)-1
    maxArea = 0

    while izquierda != derecha:
        largo = derecha - izquierda
        alto = min(height[izquierda],height[derecha])
        area = largo * alto
        maxArea = max(maxArea, area)
        if height[izquierda] <= height[derecha]:
            izquierda += 1
        else:
            derecha -= 1

    return maxArea

#Quit the innecesary min()
def maxAreaOptimizedMemory(height):
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

#Doesn´t use max() and min()
def maxAreaOptimized(height):
    capacidad_max, izquierda, derecha = 0, 0, len(height) - 1
    while (izquierda < derecha):
        if height[izquierda] <= height[derecha]:
            res = height[izquierda] * (derecha - izquierda)
            izquierda += 1
        else:
            res = height[derecha] * (derecha - izquierda)
            derecha -= 1
        if res > capacidad_max:
            capacidad_max = res
    return capacidad_max

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))