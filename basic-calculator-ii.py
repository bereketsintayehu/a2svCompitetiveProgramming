class Solution:
    def calculate(self, s: str) -> int:
        stack, opp, val = [], '+', 0
        s = s.replace(' ', '')    
        n = len(s)

        
        for i, num in enumerate(s):
            if num.isdigit():
                val = val * 10 + int(num)
                
            if not num.isdigit() or i == n - 1:
                if opp == '+':
                    stack.append(val)
                    
                elif opp == '-':
                    stack.append(-val)
                    
                elif opp == '*':
                    stack.append(stack.pop() * val)
                    
                else:
                    stack.append(int(stack.pop() / val))
                    
                val = 0
                opp = num
                
        return sum(stack)
