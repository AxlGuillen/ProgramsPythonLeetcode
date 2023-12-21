n = int(input())
medio = (n//2)+1

matriz = []
renglon = []
indice = 0

#primera mitad
for j in range(medio):
    renglon = []
    for i in range(n):
        if i == indice or i == medio-1 or i == n-1-indice and indice!=medio-1:
            renglon.append('*')
        elif indice==medio-1:
            renglon.append('*')
        else:
            renglon.append('.')
    matriz.append(renglon)
    indice = indice + 1

#segunda mitad
indice2= 0
for z in range(medio-1):
    matriz.append(matriz[medio-2-indice2])
    indice2 += 1

#imprime la matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()

