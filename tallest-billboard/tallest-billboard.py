class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}

        for rod in rods: 
            for diff, val in dp.copy().items(): 
                dp[diff + rod] = max(dp.get(diff + rod, 0), val)
                dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), val + min(rod, diff))

        return dp[0]