class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr=[]
        if m*n==len(original):
            for j in range(0,len(original),n):
                arr.append(original[j:j+n])
        return arr