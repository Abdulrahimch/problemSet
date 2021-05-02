def max_profit(prices) -> int:
    best_profit = 0
    print(prices)
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                if profit > best_profit:
                    best_profit = profit
    return best_profit
y = [2,1,2,1,0,1,2]
print(max_profit(y))
