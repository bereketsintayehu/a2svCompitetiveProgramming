class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = j = ans = 0
        gl, sl = len(g), len(s)

        while i < gl and j < sl:
            if g[i] <= s[j]:
                ans += 1
                j += 1
            i += 1

        return ans