class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                p = stack.pop()
                ans[p[1]] = i - p[1]
                
            stack.append((temperatures[i], i))
        
        return ans
        