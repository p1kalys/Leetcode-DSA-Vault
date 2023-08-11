class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def helper(index, current, evaluated, prev):
            if index == len(num):
                if evaluated == target:
                    result.append(current)
                return
            
            for i in range(index, len(num)):
                if i != index and num[index] == '0':  # Avoid leading zeros
                    break
                
                operand = int(num[index:i+1])
                
                if index == 0:
                    helper(i + 1, str(operand), operand, operand)
                else:
                    helper(i + 1, current + '+' + str(operand), evaluated + operand, operand)
                    helper(i + 1, current + '-' + str(operand), evaluated - operand, -operand)
                    helper(i + 1, current + '*' + str(operand), evaluated - prev + (prev * operand), prev * operand)
    
        result = []
        helper(0, '', 0, 0)
        return result
