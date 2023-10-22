class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = nums[k]
        i=k
        j=k
        mini = nums[k]
        n=len(nums)
        while i>0 or j<n-1:
            if (nums[i-1] if i>0 else 0) < (nums[j+1] if j<n-1 else 0):
                j+=1
            else:
                i-=1
            mini = min(mini, nums[j],nums[i])
            res = max(res, mini*(j-i+1))
        return res
