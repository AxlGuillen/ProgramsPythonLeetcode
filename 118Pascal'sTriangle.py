def generate(numRows):
    piramide = []

    for i in range(numRows):
        nivel = []
        for j in range(i+1):
            if j == 0 or j == i:
                nivel.append(1)
            else:
                numero = piramide[i-1][j-1] + piramide[i-1][j]
                nivel.append(numero)
        piramide.append(nivel)

    return piramide

def generate2(numRows):
    piramide = []

    for i in range(numRows):
        piramide.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                piramide[i].append(1)
            else:
                piramide[i].append(piramide[i-1][j-1] + piramide[i-1][j])

    return piramide

numRows = 4
print(generate2(numRows))