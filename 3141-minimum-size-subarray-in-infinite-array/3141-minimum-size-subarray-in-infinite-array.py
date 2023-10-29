class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        length = len(nums)
        numsSum = sum(nums)
        rows = target//numsSum
        total = rows * numsSum
        right, minLen = 0, float('inf')

        for idxL, left in enumerate(nums):
            while total < target:
                total += nums[right]
                if right == length -1:
                    right = 0
                    rows+=1
                else: right += 1
            if total == target:
                minLen = min(minLen, (rows * length) + right -idxL)
            total -= left
        return minLen if minLen != float('inf') else -1          