class Solution:
    keys = {'2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.res = []
        self.recursion(digits, '')
        return self.res

    def recursion(self, digits, value):
        if not digits:
            self.res.append(value)
            return 0
        ckeys = self.keys[digits[0]]
        for key in ckeys:
            self.recursion(digits[1:], value+key)