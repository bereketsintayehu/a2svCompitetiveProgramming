from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        if s[0] in [')', '}', ']']:
            return False
        
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
                
            lastPushed = stack.pop()
            if s[i] == ')' and lastPushed != '(':
                return False
            if s[i] == '}' and lastPushed != '{':
                return False
            if s[i] == ']' and lastPushed != '[':
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                
            
                                
         