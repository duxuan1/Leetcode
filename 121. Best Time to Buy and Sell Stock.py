from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit, min_price = 0, prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit