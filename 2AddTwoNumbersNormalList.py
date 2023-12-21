#My version
def addTwoNumbers( l1, l2):
    num1 = 0
    num2 = 0
    con1 = 1

    for num in l1:
        num1 = num1 + (num * con1)
        con1 = con1 * 10

    con1 = 1

    for num in l2:
        num2 = num2 + (num * con1)
        con1 = con1 * 10

    suma = num1 + num2

    lista = list(str(suma))
    lista.reverse()
    print(lista)

#Optimized version
def OptimizedAddTwoNumbers(l1, l2):
    num1 = 0
    num2 = 0

    # Convertir la lista l1 en un número entero
    for i, num in enumerate(l1):
        num1 += num * (10 ** i)

    # Convertir la lista l2 en un número entero
    for i, num in enumerate(l2):
        num2 += num * (10 ** i)

    # Sumar ambos números
    suma = num1 + num2

    # Convertir el resultado de nuevo a una lista con dígitos en orden inverso
    # Aquí, str(suma)[::-1] convierte la suma en un string y lo invierte
    lista = [int(digito) for digito in str(suma)[::-1]]

    return lista

l1 = [1,2,3]
l2 = [1,2,7]

addTwoNumbers(l1,l2)