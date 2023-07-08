class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        rev=num[::-1]
        rev=int(rev)
        s=str(rev)
        num=s[::-1]
        return num