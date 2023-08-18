class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        keys={"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        combinations=""
        if not digits:
            return []
        def recursion(i,digits,combinations):
            if i==len(digits):
                res.append(combinations[:])
                return
            for letter in keys[digits[i]]:
                recursion(i+1,digits,combinations+letter)
        recursion(0,digits,combinations)
        return res