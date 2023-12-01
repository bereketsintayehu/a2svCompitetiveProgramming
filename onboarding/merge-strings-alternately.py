class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        n = min(len(word1), len(word2))

        while i < n:
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1

        ans.append(word1[i:])
        ans.append(word2[i:])

        return ''.join(ans)
        