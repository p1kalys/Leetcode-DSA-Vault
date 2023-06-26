class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        Fuel=0
        stop_Fuel=0
        start=0
        for i in range(n):
            Fuel+=gas[i]-cost[i]
            stop_Fuel+=gas[i]-cost[i]
            if stop_Fuel<0:
                stop_Fuel=0
                start=i+1
        return -1 if Fuel<0 else start