class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                res += stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
                
            elif op == "C":
                res -= stack[-1]
                stack.pop()
                
            elif op == "D":
                res += stack[-1]*2
                stack.append(stack[-1]*2)
                
            else:
                stack.append(int(op))
                res += int(op)
        
        return res

        