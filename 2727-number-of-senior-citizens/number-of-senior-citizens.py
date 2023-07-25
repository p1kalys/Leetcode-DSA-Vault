class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if int(i[11]) > 6:
                count += 1
            elif int(i[11]) == 6 and int(i[12]) > 0:
                count += 1
        return count