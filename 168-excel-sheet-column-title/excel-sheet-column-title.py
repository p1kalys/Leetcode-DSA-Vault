class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res=""
        while columnNumber:
            columnNumber-=1
            res+=chars[columnNumber % 26]
            columnNumber//=26
        return res[::-1]