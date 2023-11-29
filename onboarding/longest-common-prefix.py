class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        i = 0
        try:
            while True:
                for j in range(1, len(strs)):
                    if strs[j][i] != strs[j-1][i]:
                        return ''.join(ans)
                else:
                    ans.append(strs[0][i])
                i += 1
        except IndexError:
            return ''.join(ans)
        