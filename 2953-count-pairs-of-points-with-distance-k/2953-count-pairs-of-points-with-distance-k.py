class Solution:
    def countPairs(self, coordinates, k):
        result = 0
        seen = {}
        for x, y in coordinates:
            for split in range(k + 1):
                x_complement = x ^ split
                y_complement = y ^ (k - split)
                result += seen.get((x_complement, y_complement), 0)
            seen[x, y] = seen.get((x, y), 0) + 1
        return result