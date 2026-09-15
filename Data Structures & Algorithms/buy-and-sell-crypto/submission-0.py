class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        min_price = prices[0]

        for i in range(0,len(prices)-1):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit, prices[i+1]-min_price)

        return max_profit