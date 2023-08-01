class Solution:
    def helper(self, i, n, k, ans, slate):
        if k==len(slate):
            ans.append(slate[:])
            return 
        if i==n+1:
            return 
        slate.append(i)
        self.helper(i+1,n,k,ans,slate)
        slate.pop()
        self.helper(i+1,n,k,ans,slate)
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        slate=[]
        self.helper(1,n,k,ans,slate)
        return ans