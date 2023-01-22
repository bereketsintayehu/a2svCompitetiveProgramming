from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i in operators:
                y = stack.pop()
                x = stack.pop()
                if i == '-':
                    val = x - y
                if i == '+':
                    val = x + y
                if i == '*':
                    val = x * y
                if i == '/':
                    val = int(x / y)
                stack.append(val)
            else:
                stack.append(int(i))
        return stack[0]
        