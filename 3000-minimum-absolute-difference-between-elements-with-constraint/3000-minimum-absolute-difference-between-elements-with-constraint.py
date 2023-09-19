from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x==0:return 0
        n=len(nums)
        s=SortedList()
        ans=inf
        for i in range(n):
            j=s.bisect_left(nums[i])
            if j<len(s):
                ans=min(ans,abs(s[j]-nums[i]))
            if j>0:
                ans=min(ans,abs(s[j-1]-nums[i]))
            if i>=x-1:
                s.add(nums[i-(x-1)])
            # print(s,ans)
        return ans