class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        mini,maxi=1,max(quantities)
        while mini<maxi:
            mid=mini+(maxi-mini)//2
            stores=sum([ceil(q/mid) for q in quantities])
            if stores<=n:
                maxi=mid
            else:
                mini=mid+1
        return maxi