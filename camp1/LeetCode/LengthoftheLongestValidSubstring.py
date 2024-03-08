class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        def helper(l, r):
            n = r - l + 1
            for i in range(l, r):
                for j in range(l, r):
                    if word[i : j + 1] in forbidden:
                        return False
            return True
        
        ans = 0
        start = 0

        for end in range(len(word)):
            while not helper(max(start, end - 10), end + 1):
                start += 1

            ans = max(ans, end - start + 1)
        
        return ans