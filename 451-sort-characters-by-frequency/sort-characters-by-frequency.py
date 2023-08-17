class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        ans = []
        for i,j in d.items():
            ans.append([j,i])
        s = ""
        ans.sort(key = lambda x:x[0], reverse=True)
        for i in ans:
            while i[0]>0:
                s+=i[1]
                i[0]-=1
        return s 