class Solution:
    def partitionString(self, s: str) -> int:
        sub, ans = set(), 1
        
        for c in s:
            if c in sub:
                ans += 1
                sub.clear()
                sub.add(c)
            else:
                sub.add(c)
        
        return ans
        
        