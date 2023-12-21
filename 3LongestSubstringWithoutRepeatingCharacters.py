def longitudSubcadenaMasLarga(s):
    # Crear un diccionario para guardar la última posición de cada carácter
    ultima_posicion = {}
    # Iniciar el inicio de la ventana y la longitud máxima
    inicio = longitud_maxima = 0

    # Iterar a través de la cadena
    for i, caracter in enumerate(s):
        # Si el carácter está en el diccionario y inicio es menor o igual a la última posición del carácter
        if caracter in ultima_posicion and inicio <= ultima_posicion[caracter]:
            # Mover el inicio al siguiente de la última posición del carácter
            inicio = ultima_posicion[caracter] + 1
        else:
            # Calcular la nueva longitud máxima
            longitud_maxima = max(longitud_maxima, i - inicio + 1)
        # Actualizar la última posición del carácter
        ultima_posicion[caracter] = i

    # Devolver la longitud máxima encontrada
    return  longitud_maxima

# Ejemplo de uso de la función
entrada = "pwxawkew"
print(f"Entrada: {entrada}")
print(f"Salida: {longitudSubcadenaMasLarga(entrada)}")