class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        n = len(s)
        end = s.count('1')
        curr = 0

        for i in range(n):
            if s[i] == '1':
                ans += (i - curr) * (n - end - (i - curr))
                curr += 1
            else:
                ans += curr * (end - curr)
        
        return ans