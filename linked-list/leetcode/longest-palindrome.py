class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        f = 0

        for c in cnt.values():
            if c % 2 == 0:
                ans += c
            else:
                f = 1
                ans += c - 1
        
        return ans + 1 if f else ans