class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # Checking for lower buy value
            if (buy > prices[i]):
                buy = prices[i]
    
            # Checking for higher profit
            elif (prices[i] - buy > max_profit):
                max_profit = prices[i] - buy
        return max_profit