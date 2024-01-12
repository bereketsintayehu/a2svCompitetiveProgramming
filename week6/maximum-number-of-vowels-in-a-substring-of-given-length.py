class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = curr = 0
        vowel = set("aeiouAEIOU")
        
        for i, l in enumerate(s):
            if l in vowel:
                curr += 1
            if i >= k - 1:
                ans = max(ans, curr)
                if s[i - k + 1] in vowel:
                    curr -= 1
        
        return ans