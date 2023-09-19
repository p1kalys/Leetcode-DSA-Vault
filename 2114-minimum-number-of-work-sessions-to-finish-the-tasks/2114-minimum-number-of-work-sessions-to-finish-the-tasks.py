class Solution:
    def minSessions(self, tasks: List[int], k: int) -> int:
        n = len(tasks)
        l=0
        h=n
        ans=-1
        
        def f(i,sessions,k):
            if i==len(tasks):
                return True
            for j in range(len(sessions)):
                if sessions[j]+tasks[i]<=k:
                    sessions[j]+=tasks[i]
                    if f(i+1,sessions,k):
                        return True
                    sessions[j]-=tasks[i]
                if sessions[j]==0:
                    break
            return False
        
        while l<=h:
            mid = l+(h-l)//2
            sessions = [0]*mid
            if f(0,sessions,k):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans