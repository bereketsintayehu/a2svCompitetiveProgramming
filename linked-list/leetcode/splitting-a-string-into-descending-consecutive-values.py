class Solution:
    def splitString(self, s: str) -> bool:
        cur = []

        def backtrack(i):
            if i == len(s):
                return len(cur) > 1
            
            for k in range(i, len(s)):
                t = int(s[i:k + 1])
                if cur and cur[-1] - t != 1:
                    continue

                cur.append(t)
                if backtrack(k + 1):
                    return 1
                cur.pop()

        return backtrack(0)
