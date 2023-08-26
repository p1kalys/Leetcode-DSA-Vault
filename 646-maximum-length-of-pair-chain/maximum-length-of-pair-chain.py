class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        interval = [pairs[0]]

        in1,ind2 = pairs[0]

        for i in range(1, len(pairs)):
            if ind2 < pairs[i][0]:
                ind1, ind2 = pairs[i]
                interval.append(pairs[i])
        
        return len(interval)