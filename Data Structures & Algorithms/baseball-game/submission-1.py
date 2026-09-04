class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        preSum = []

        for op in operations:
            if op == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(op))
                if preSum:
                    preSum.append(preSum[-1]+int(op))
                else:
                    preSum.append(int(op))
        
        return sum(stack)

        