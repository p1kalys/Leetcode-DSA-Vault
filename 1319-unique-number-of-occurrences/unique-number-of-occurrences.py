class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        s=set()
        for i in d.values():
            s.add(i)
        return True if len(s)==len(d) else False
        
            