import math 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i+1 for i in range(n)]
        return self.getPermutation2(k-1, nums) # we want k be 0-indexed
    
    def getPermutation2(self, k, nums) -> str:
        n = len(nums) 
        if n == 1: 
            return str(nums[0])
        if k == 0: return "".join([str(i) for i in nums]) # shortcut for speeding up
        p_n_1 = math.factorial(n-1) # permutations of n-1 
        idx = k//p_n_1  # idx of the chosen digit
        return str(nums[idx]) + self.getPermutation2(k%p_n_1, nums[:idx]+nums[idx+1:])
        