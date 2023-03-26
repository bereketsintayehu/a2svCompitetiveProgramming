class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        stack = []
        
        for i in range(len(num)):
            while k > 0 and len(stack) > 0 and stack[len(stack)-1] > num[i]:
                stack.pop()
                k -= 1
                
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1
        
        if len(stack) == 1:
            return stack[0]
        
        return ''.join(stack).lstrip('0') or '0'
