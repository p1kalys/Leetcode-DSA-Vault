class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        n=len(arr)
        for i in range(n-2):
            if arr[i]==arr[i-1] and i>0:
                continue
            left=i+1
            right=n-1
            while left<right:
                curr_sum=arr[i]+arr[left]+arr[right]
                if curr_sum==0 and [arr[i],arr[left],arr[right]] not in res:
                    res.append([arr[i],arr[left],arr[right]])
                    left+=1
                    right-=1
                elif curr_sum>0:
                    right-=1
                else:
                    left+=1
        return res