class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i=0
        j=0
        ans=0
        cF=0
        cT=0
        while j < len(answerKey):
            if answerKey[j]=='F':
                cF+=1
            else:
                cT+=1
            while min(cT,cF)>k:
                if answerKey[i]=='F':
                    cF-=1
                else:
                    cT-=1
                i+=1
            ans=max(cT+cF,ans)
            j+=1
        return ans
