class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=set()
        Sum=sum(nums)
        dp.add(0)
        if Sum%2:
            return False
        target=Sum//2
        for i in range(len(nums)-1,-1,-1):
            Next=set()
            for t in dp:
                if (t+nums[i]==target): return True
                Next.add(t+nums[i])
                Next.add(t)
            dp=Next
        return True if target in dp else False
