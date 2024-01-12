class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if m < n:
            return ""

        target = Counter(t)
        curr = Counter()

        start, end = m, m
        ans = m + 1
        windowStart = 0
        
        for windowEnd in range(m):
            if s[windowEnd] in target:
                curr[s[windowEnd]] += 1
            
            while all(curr[key] >= target[key] for key in target.keys()):
                temp = windowEnd - windowStart + 1
                if ans > temp:
                    start, end = windowStart, windowEnd
                    ans = temp

                if s[windowStart] in target:
                    curr[s[windowStart]] -= 1
                windowStart += 1

        if all(curr[key] >= target[key] for key in target.keys()):
            if ans > (windowEnd - windowStart + 1):
                start, end = windowStart, windowEnd

        return s[start:end+1] 


