class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - smallest)
                smallest = min(smallest, cur)
        return res