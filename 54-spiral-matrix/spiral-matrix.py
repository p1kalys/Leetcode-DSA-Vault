class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total_elements=len(matrix)*len(matrix[0])
        cur_count=0
        result=[]
        min_row,min_col=0,0
        max_row,max_col=len(matrix),len(matrix[0])
        while cur_count<total_elements:
            #left-->right
            for itr1 in range(min_col,max_col):
                result.append(matrix[min_row][itr1])
                cur_count+=1
            min_row+=1
            #top--->down
            for itr2 in range(min_row,max_row):
                result.append(matrix[itr2][max_col-1])
                cur_count+=1
            max_col-=1
            #right--->left
            if cur_count<total_elements:
                for itr3 in range(max_col-1,min_col-1,-1):
                    result.append(matrix[max_row-1][itr3])
                    cur_count+=1
                max_row-=1
            #down--->up
            if cur_count<total_elements:
                for itr4 in range(max_row-1,min_row-1,-1):
                    result.append(matrix[itr4][min_col])
                    cur_count+=1
                min_col+=1
        return result