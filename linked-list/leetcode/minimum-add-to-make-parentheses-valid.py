class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = op = 0

        for b in s:
            if b == '(':
                op += 1
            else:
                if op:
                    op -= 1
                else:
                    ans += 1

        return ans + op