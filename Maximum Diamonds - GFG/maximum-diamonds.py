#User function Template for python3
import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        max_heap=[-a for a in A]
        heapq.heapify(max_heap)
        # code here 
        s=0
        while K>0:
            diamonds=-heapq.heappop(max_heap)
            s+=diamonds
            diamonds//=2
            heapq.heappush(max_heap,-diamonds)
            K-=1
        return s
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends