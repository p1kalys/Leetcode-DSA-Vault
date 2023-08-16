class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ""

        for i in s:
            if not i.isspace():
                word += i
            elif i.isspace() and word != "":
                stack.append(word)
                word = ""
            else:
                continue
        
        if word != "":
            stack.append(word)
        
        word = ""
        for i in range(len(stack)-1,0,-1):
            word +=stack[i]
            word+=" "

        word += stack[0]
        return word