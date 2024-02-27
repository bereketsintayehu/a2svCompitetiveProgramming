class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        m = 0
        for i in range(n):
            left[i] = m
            m = max(m, height[i])
        
        m = 0
        for i in range(n - 1, -1, -1):
            right[i] = m
            m = max(m, height[i])
        
        ans = 0
        for i in range(n):
            ans += max(0, min(right[i], left[i]) - height[i])

        return ans