def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    max_profit = 0
    for sell in prices[1:]:
        if sell > buy:
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
        else:
            buy = sell
    return max_profit


ls = [7, 1, 5, 3, 6, 4]
print(maxProfit(ls))
