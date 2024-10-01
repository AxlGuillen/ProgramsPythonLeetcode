"""

    Convierte un número romano a un entero utilizando una estrategia que suma
    los valores de los símbolos romanos y corrige las combinaciones especiales.

    Argumentos:
    romanNumber (str): El número romano que se desea convertir.

    Retorno:
    int: El valor entero del número romano.

"""

def romanToIntMyVersion(romanNumber):
    """
        - Primero, define un diccionario `valuesInRoman` que incluye tanto los valores
          de los símbolos romanos individuales ('I', 'V', 'X', etc.), como las combinaciones
          especiales ('IV', 'IX', 'XL', etc.). En el caso de las combinaciones especiales,
          los valores están configurados como negativos (-2, -20, -200) porque se ajustan después
          de la suma de todos los símbolos romanos.
        - Luego, se suma el valor de cada símbolo individual en el número romano.
        - Después, el código corrige las combinaciones especiales ('IV', 'IX', etc.)
          sumando sus valores negativos cuando se detectan en el número romano.
    """

    valuesInRoman = {
        "I": 1,
        "IV": -2,
        "V": 5,
        "IX": -2,
        "X": 10,
        "XL": -20,
        "L": 50,
        "XC": -20,
        "C": 100,
        "CD": -200,
        "D": 500,
        "CM": -200,
        "M": 1000
    }
    matches = ["IV", "IX", "XL", "XC", "CD", "CM"]
    value = 0

    # Suma los valores de cada símbolo individual en el número romano
    for symbol in romanNumber:
        value += valuesInRoman[symbol]

    # Corrige las combinaciones especiales
    for match in matches:
        if match in romanNumber:
            value += valuesInRoman[match]

    return value


def romanToIntOptimizedVersion(s):
    res = 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Iteramos sobre pares consecutivos de caracteres
    for a, b in zip(s, s[1:]):
        if roman[a] < roman[b]:
            res -= roman[a]
        else:
            res += roman[a]

        # Añadimos el valor del último carácter
    return res + roman[s[-1]]



numberInRoman = "XL"

print(romanToIntMyVersion(numberInRoman))
print(romanToIntOptimizedVersion(numberInRoman))