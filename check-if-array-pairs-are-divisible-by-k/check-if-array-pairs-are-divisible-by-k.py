from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        counter = defaultdict(int)
        for a in arr:
            rem = (a % k + k) % k
            counter[rem] += 1
        for rem, value in counter.items():
            if rem == 0 and value % 2 != 0:
                return False
            if rem != 0 and counter[rem] != counter[k - rem]:
                return False
        return True
