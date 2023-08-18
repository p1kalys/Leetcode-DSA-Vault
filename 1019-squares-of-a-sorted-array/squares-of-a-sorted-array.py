class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        ans = []
        while start <= end:
            ele1 = nums[start]**2
            ele2 = nums[end]**2
            if ele1 < ele2:
                ans.append(ele2)
                end -= 1
            else:
                ans.append(ele1)
                start += 1
        ans.reverse()
        return ans