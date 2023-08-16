class Solution:
    def calculate(self, s: str) -> int:
        output, current, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                current = current * 10 + int(c)
            elif c == "+":
                output += (current * sign)
                current = 0
                sign = 1
            elif c == "-":
                output += (current * sign)
                current = 0
                sign = -1
            elif c == "(":
                stack.append(output) 
                stack.append(sign)
                output = 0
                sign = 1
            elif c == ")":
                output += (current * sign)
                output *= stack.pop()
                output += stack.pop()
                current = 0
        if current :
            output += (current * sign)
        return output 