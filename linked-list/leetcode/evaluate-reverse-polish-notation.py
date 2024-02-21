class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp = {
            '*': lambda x, y: x * y,
            '-': lambda x , y: x - y,
            '/': lambda x, y: int(x / y),
            '+': lambda x, y: x + y
        }

        for token in tokens:
            if token in opp:
                y = stack.pop()
                x = stack.pop()

                stack.append(opp[token](x, y))
            else:
                stack.append(int(token))

        return stack[0]
        