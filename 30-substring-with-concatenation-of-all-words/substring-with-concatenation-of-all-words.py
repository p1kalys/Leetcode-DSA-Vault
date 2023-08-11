class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        d = {}
        for word in words:
            if word in d:
                d[word] +=1
            else:
                d[word] = 1
        
        i = 0
        j = len(words[0])*len(words) - 1

        while j < len(s):
            tmp = {}
            a = i
            b = i+len(words[0])-1

            while b <= j:
                cur = s[a:b+1]
                if cur in tmp:
                    tmp[cur] +=1
                else:
                    tmp[cur] = 1
                a = b+1
                b = b+len(words[0])
            
            if tmp == d:
                output.append(i)
            i+=1
            j+=1
        
        return output