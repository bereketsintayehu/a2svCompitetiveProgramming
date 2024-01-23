class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        oneCount = s.count('1')
        oneCount -= s[0] == '1'
        zeroCount = s[0] == '0'
        ans = oneCount

        for i in range(1, len(s)):
            ans = max(ans, oneCount + zeroCount)
            zeroCount += s[i] == '0' 
            oneCount += -1 if s[i] == '1' else 0
        
        return ans