def find(index,candidates,target,Sum,slate,res):
    if Sum==target:    
        res.append(slate[:])
        return 
    elif Sum>target:
        return
    for i in range(index,len(candidates)):
        Sum+=candidates[i]
        slate.append(candidates[i])
        find(i,candidates,target,Sum,slate,res)
        slate.pop()
        Sum-=candidates[i]

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        slate=[]
        res=[]
        Sum=0
        find(0,candidates,target,Sum,slate,res)
        return res
    