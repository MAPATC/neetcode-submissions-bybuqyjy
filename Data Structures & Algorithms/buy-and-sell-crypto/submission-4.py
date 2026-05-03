class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        best_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < best_price:
                best_price = prices[i]
            if max_profit < (prices[i] - best_price):
                max_profit = prices[i] - best_price
        return max_profit