def maxProfitNotOptimized(prices):
    """
    Calcula el máximo beneficio posible de comprar y vender una acción, sin optimizar.

    Este método busca todos los precios de compra posibles (menores que el precio de venta siguiente)
    y luego para cada precio de compra, busca el máximo precio de venta posible después de la compra.
    Finalmente, calcula el beneficio para cada par de compra/venta y devuelve el máximo beneficio encontrado.

    Parámetros:
    - prices: Lista de enteros representando el precio de la acción en cada día consecutivo.

    Devuelve:
    - El máximo beneficio posible de una sola operación de compra y venta. Si no es posible obtener beneficio,
      devuelve 0.

    Nota: Este enfoque no está optimizado y puede ser ineficiente para grandes listas de precios.
    """

    menores = {}
    rendimientos = []
    menor = 0
    mayor = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            menor = prices[i]
            menores[i] = menor

    for indice, valor in menores.items():
        mayor = 0
        for i in range(indice + 1, len(prices)):
            if prices[i] > mayor:
                mayor = prices[i]
        rendimientos.append(mayor - valor)

    if not rendimientos:
        return 0

    return max(rendimientos)


def maxProfit(prices):
    """
    Calcula el máximo beneficio posible de comprar y vender una acción, optimizado.

    Este método itera a través de la lista de precios una sola vez. Mantiene dos punteros:
    uno para el día de compra (`left`) y uno para el día de venta (`right`), inicialmente en los dos primeros días.
    Si el precio en `right` es mayor que en `left`, calcula el beneficio y actualiza el beneficio máximo si es necesario.
    Si el precio en `right` es menor o igual que en `left`, mueve el puntero `left` a `right`, considerando un nuevo día de compra.
    El puntero `right` se mueve hacia adelante en cada iteración para considerar el siguiente día de venta.

    Parámetros:
    - prices: Lista de enteros representando el precio de la acción en cada día consecutivo.

    Devuelve:
    - El máximo beneficio posible de una sola operación de compra y venta. Si no es posible obtener beneficio,
      devuelve 0.
    """

    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


# Ejemplo de uso
prices = [3, 2, 6, 5, 0, 3]
print("Máximo beneficio optimizado:", maxProfit(prices))
