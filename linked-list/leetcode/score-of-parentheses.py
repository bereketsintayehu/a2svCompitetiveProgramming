class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = -1
        ans = 0

        for i, b in enumerate(s):
            if b == ')':
                if i - stack.pop() == 1:
                    ans += 2 ** curr
                curr -= 1
            else:
                curr += 1
                stack.append(i)

        return ans