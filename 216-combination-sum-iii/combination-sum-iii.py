class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(i, cur):            
            if sum(cur)  > n  or len(cur)  > k: 
                return
            if sum(cur) == n and len(cur) == k:
                res.append(cur)
                return
            for j in range(i, len(nums)):     
                dfs(j + 1, cur + [nums[j]])         
        res    = []
        nums   = [i   for i in range(1, 10)] 
        dfs(0, [])
        return res