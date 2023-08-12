class Solution:
    def partitionString(self, s: str) -> int:
        cur=set()
        res=1
        for i in s:
            if i in cur:
                res+=1
                cur=set()
            cur.add(i)
        return res