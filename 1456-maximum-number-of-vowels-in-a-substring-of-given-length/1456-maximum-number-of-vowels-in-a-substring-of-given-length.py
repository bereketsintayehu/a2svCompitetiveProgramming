class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_count = 0
        curr_count = 0
        
        def isVowel(l):
            return l in "aeiouAEIOU"
        
        for i, l in enumerate(s):
            if isVowel(l):
                curr_count += 1
            if i >= k - 1:
                max_count = max(max_count, curr_count)
                if isVowel(s[i-k+1]):
                    curr_count -= 1
        
        return max_count