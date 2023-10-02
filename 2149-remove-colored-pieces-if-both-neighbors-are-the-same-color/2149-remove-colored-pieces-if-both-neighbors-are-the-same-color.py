class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c1=0
        c2=0
        a=0
        b=0
        for i in range(len(colors)):
            if colors[i]=='A':
                c1+=1
            else:
                c2+=1
            if colors[i]!='A' or i==len(colors)-1:
                if c1>2:
                    a+= c1-2
                c1=0
            if colors[i]!='B' or i==len(colors)-1:
                if c2>2:
                    b+= c2-2
                c2=0
        return a>b