class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=[]
        i=0
        for j in range(len(nums)):
            if (j-i) > k:
                d.remove(nums[i])
                i+=1
            if nums[j] in d:
                return True
            d.append(nums[j])

        return False