class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n=len(intervals)
        count=1
        j=0
        for i in range(1,n):
            if intervals[i][0]>=intervals[j][1]:
                j=i
                count+=1
        return n-count