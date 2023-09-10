class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        res = 1 #base case

        while slots:
            valid_choices = slots * (slots - 1) // 2            
            res *= valid_choices
            slots -= 2
        return res % (10**9 + 7)