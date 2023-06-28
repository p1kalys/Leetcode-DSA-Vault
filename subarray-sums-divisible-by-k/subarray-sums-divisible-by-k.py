class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = defaultdict(int) # set()
        pref = 0
        count = 0
        s[0] = 1

        for i, n in enumerate(nums):
            pref += n
            target = pref%k

            if target < 0: target += k

            if target in s: count += s[target]

            s[target] += 1

        return count