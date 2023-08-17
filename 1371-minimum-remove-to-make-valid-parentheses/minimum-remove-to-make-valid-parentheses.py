class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        list_str = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    list_str[i] = ""
        for i in stack:
            list_str[i] = ""
        return ''.join(list_str)