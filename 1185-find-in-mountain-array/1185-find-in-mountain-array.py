# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        ar_len = mountain_arr.length()
        l, r = 1, ar_len - 2
        
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountain_arr.get(m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        l, r = peak, ar_len - 1 

        while l <= r:
            m = (l + r) // 2
            val = mountain_arr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1
        