def maxProfitNotOptimized(prices):
    menores = {}
    rendimientos = []
    menor = 0
    mayor = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            menor = prices[i]
            menores[i]=menor

    for indice,valor in menores.items():
        mayor = 0
        for i in range(indice+1, len(prices)):
            if prices[i] > mayor:
                mayor = prices[i]
        rendimientos.append(mayor-valor)


    if not rendimientos:
        return 0

    return max(rendimientos)

def maxProfit(prices):
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

prices = [3,2,6,5,0,3]
print(maxProfit(prices))