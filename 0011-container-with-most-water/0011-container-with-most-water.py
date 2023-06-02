class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            ans = max(area, ans)
        
        return ans