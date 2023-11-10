class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for i,j in adjacentPairs:
            d[i].append(j)
            d[j].append(i)
        res=[]
        root=None
        for num in d:
            if len(d[num])==1:
                root=num
                break
        def dfs(node,prev,res):
            res.append(node)
            for n in d[node]:
                if n!=prev:
                    dfs(n,node,res)
        dfs(root,None,res)
        return res
