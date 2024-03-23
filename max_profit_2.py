def maxProfit(prices: list[int]) -> int:
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[sell] - prices[buy] > 0:
            profit = prices[sell] - prices[buy]
            max_profit += profit
        buy = sell
        sell += 1
    return max_profit


ls1 = [7, 1, 5, 3, 6, 4]
ls2 = [1, 2, 3, 4, 5]
ls3 = [7, 6, 4, 3, 1]
print(maxProfit(ls1))
print(maxProfit(ls2))
print(maxProfit(ls3))

