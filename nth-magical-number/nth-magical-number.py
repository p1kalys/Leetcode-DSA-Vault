class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        x = 10 ** 9 + 7
        low=min(a,b)
        high=n*min(a,b)
        lcm=math.lcm(a,b)
        while (low<=high):
            mid = low + (high-low) // 2
            if (mid//a)+(mid//b)-(mid//lcm)<n:
                low=mid+1
            else:
                high=mid-1
                ans=mid
        return ans%x