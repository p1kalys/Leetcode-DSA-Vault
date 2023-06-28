class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix)-1
        while i<=j:
            l=0
            r=len(matrix[0])-1
            if target<=matrix[i][r] and target>=matrix[i][l]:
                while l<=r:
                    mid=l+(r-l)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        l=mid+1
                    else:
                        r=mid-1
            i+=1
        return False

