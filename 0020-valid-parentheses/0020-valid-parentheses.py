from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        if s[0] in closing:
            return False
        
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
                
            lastPushed = stack.pop()
            
            if s[i] == closing[0] and lastPushed != opening[0]:
                return False
            if s[i] == closing[1] and lastPushed != opening[1]:
                return False
            if s[i] == closing[2] and lastPushed != opening[2]:
                return False
            
        
        if len(stack) == 0:
            return True
        else:
            return False
                
            
                                
         