class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        index_map = {}

        for r in range(len(s)):
            if s[r] in index_map:
                l = max(l, index_map[s[r]] + 1)
            
            index_map[s[r]] = r

            ans = max(ans, r - l + 1)

        return ans