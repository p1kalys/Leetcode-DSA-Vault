class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                prev=st.pop()
                c=s[i]
                if c=='}' and prev!='{':
                    return False
                elif c==')' and prev!='(':
                    return False
                elif c==']' and prev!='[':
                    return False
        return len(st)==0