class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        cnt = Counter()
        ans = ''
        m = 0
        def helper(st):
            t = set(st)
            for c in st:
                if c.isupper() and chr(ord(c) + 32) not in t:
                    return False
                if c.islower() and chr(ord(c) - 32) not in t:
                    return False
            
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j + 1]
                if helper(st):
                    n = j - i + 1
                    if n > m:
                        m = n
                        ans = st
        
        return ans


