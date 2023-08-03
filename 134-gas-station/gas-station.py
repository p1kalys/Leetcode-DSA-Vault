class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        balance=0
        deficit=0
        for i in range(len(gas)):
            balance+=gas[i]-cost[i]
            if balance<0:
                deficit+=balance
                start=i+1
                balance=0
        if deficit+balance>=0:
            return start
        return -1    