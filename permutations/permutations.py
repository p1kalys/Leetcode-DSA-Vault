from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        permut=permutations(nums)
        for i in list(sorted(set(permut))):
            res.append(i)
        return res
        