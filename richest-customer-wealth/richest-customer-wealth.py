class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich_wealth=0
        for i in range(len(accounts)):
            s=sum(accounts[i])
            rich_wealth=max(rich_wealth,s)
        return rich_wealth
