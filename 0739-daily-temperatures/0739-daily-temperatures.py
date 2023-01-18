from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        answer = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                poped = stack.pop()
                answer[poped[1]] = i - poped[1]
                
            stack.append([temperatures[i], i])
        
        return answer
        