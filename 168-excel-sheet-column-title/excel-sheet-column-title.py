class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while columnNumber:
            columnNumber -= 1
            result = chars[columnNumber % 26] + result
            columnNumber //= 26
        return result