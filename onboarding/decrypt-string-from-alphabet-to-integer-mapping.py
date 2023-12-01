class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        n = len(s) 
        i = 0

        while i < n:
            if i+2 < n and s[i+2] == '#':
                ans.append(chr(96+int(s[i]+s[i+1])))
                i += 3

            else:
                ans.append(chr(96+int(s[i])))
                i += 1


        return ''.join(ans)