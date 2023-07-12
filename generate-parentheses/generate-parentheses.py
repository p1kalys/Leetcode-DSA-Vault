class Solution:
    def generateParenthesis(self, n):
        self.ans = []
        s = ""
        self.generate(s, n, n)
        return self.ans

    def generate(self, s, o, c):
        if o == 0 and c == 0:
            self.ans.append(s)
            return
        if o > 0:
            s += '('
            self.generate(s, o - 1, c)
            s = s[:-1]
        if c > 0:
            if o < c:
                s += ')'
                self.generate(s, o, c - 1)
                s = s[:-1]
