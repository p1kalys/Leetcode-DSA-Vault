class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target and nums[mid] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target and nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1