from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        for i in range(len(s)):
            if s[i] == ')':
                combined = ''
                while len(stack) > 0 and stack[-1] != '(':
                    poped = stack.pop()[::-1]
                    combined += poped
                stack.pop()
                stack.append(combined)
            else:
                stack.append(s[i])        
        
        return ''.join(stack)
        
        
        