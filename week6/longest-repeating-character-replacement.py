class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = max_char = longest_substring = 0
        freq_map = Counter()

        for r in range(len(s)):
            freq_map[s[r]] += 1

            max_char = max(max_char, freq_map[s[r]])

            while r - l + 1 - max_char > k:
                freq_map[s[l]] -= 1
                l += 1

            longest_substring = max(longest_substring, r - l + 1)
        
        return longest_substring