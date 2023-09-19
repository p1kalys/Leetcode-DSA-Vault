class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        ans=[]
        if len(arr)<4:
            return ans
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                k=j+1
                l=n-1
                while k<l:
                    s=arr[i]+arr[j]+arr[k]+arr[l]
                    if s==target and [arr[i],arr[j],arr[k],arr[l]] not in ans:
                        ans.append([arr[i],arr[j],arr[k],arr[l]])
                        k+=1
                        l-=1
                    elif s>target:
                        l-=1
                    else:
                        k+=1
        
        return ans