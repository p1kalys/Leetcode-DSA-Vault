class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = float('inf')
        self.count = [0] * k

        self.backtrack(0, cookies, k)
        return self.ans

    def backtrack(self, cookieNumber, cookies, k):
        if cookieNumber == len(cookies):
            maximum = max(self.count)
            self.ans = min(self.ans, maximum)
            return

        for i in range(k):
            self.count[i] += cookies[cookieNumber]
            self.backtrack(cookieNumber + 1, cookies, k)
            self.count[i] -= cookies[cookieNumber]
            if self.count[i] == 0:
                break