class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i, cur):            
            if sum(cur)  > n  or len(cur)  > k: # sum or length exceeded --> exit    
                return
            if sum(cur) == n and len(cur) == k: # we found solution      --> add to result's array
                res.append(cur)
                return
            for j in range(i, len(nums)):       # we iterate from the left to the right             
                dfs(j + 1, cur + [nums[j]])          # next element will be bigger (j + 1) than current
        res    = []
        nums   = [i   for i in range(1, 10)]   # create array [1,2,3,4,5,6,7,8,9]
        dfs(0, [])
        return res