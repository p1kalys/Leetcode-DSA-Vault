class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        n = len(positions)

        ind = sorted(range(n) , key=positions.__getitem__)

        for i in ind:
            while stack and directions[stack[-1]] == 'R' and directions[i] == 'L' and healths[i] != 0:
                diff = healths[stack[-1]] - healths[i]

                if diff == 0:
                    healths[i] = 0
                    healths[stack[-1]] = 0
                    stack.pop()
                if diff < 0:
                    healths[stack[-1]] = 0
                    healths[i] -= 1
                    stack.pop()
                if diff > 0:
                    healths[stack[-1]] -= 1
                    healths[i] = 0
            
            if healths[i] != 0:
                stack.append(i)

        ans = []
        for h in healths:
            if h != 0:
                ans.append(h)

        return  ans