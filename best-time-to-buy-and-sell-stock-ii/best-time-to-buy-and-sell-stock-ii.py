class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans,flag,buy = 0, 0, 10 ** 10
        if len(prices) <= 1:
            return 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                if not flag:
                    flag = 1
                    buy = prices[i]
            else:
                if flag:
                    flag = 0
                    ans += prices[i] - buy
                    buy = 10 **  10
        ans += (prices[i + 1] - buy > 0) * (prices[i + 1] - buy)
        return ans
                