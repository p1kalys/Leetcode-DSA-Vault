class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(nums[i]+pref[-1])
        ans = []
        for i in range(len(pref)):
            if i < k or i > len(pref)-1-k:
                ans.append(-1)
            else:
                ans.append((pref[i+k]-pref[i-k]+nums[i-k])//(2*k+1))
        return ans
            


