class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        preSum = [0]

        for op in operations:
            if op == "+":
                preSum.append(preSum[-1]+int(stack[-1])+int(stack[-2]))
                stack.append(int(stack[-1])+int(stack[-2]))
                
            elif op == "C":
                stack.pop()
                preSum.pop()
            elif op == "D":
                preSum.append(preSum[-1]+(int(stack[-1])*2))
                stack.append(int(stack[-1])*2)
                
            else:
                stack.append(int(op))
                if not preSum:
                    preSum.append(int(op))
                else:
                    preSum.append(preSum[-1]+int(op))
        
        return preSum[-1]

        