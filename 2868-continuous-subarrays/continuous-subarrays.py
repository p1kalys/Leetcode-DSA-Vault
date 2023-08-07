class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        freq_map = {}
        count = 0
        
        for right in range(len(nums)):
            # Increment frequency of nums[right] in freq_map
            freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1
            
            # Find the maximum and minimum values in the current window
            max_val = max(freq_map)
            min_val = min(freq_map)
            
            # Check if conditions are satisfied
            while max_val - min_val > 2:
                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]
                left += 1
                max_val = max(freq_map)
                min_val = min(freq_map)
            
            # Increment count
            count += right - left + 1
        
        return count
