class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""

        ans += s[:spaces[0]]
        ans += " "

        for i in range(1, len(spaces)):
            ans += s[spaces[i-1]:spaces[i]]
            ans += " "

        ans += s[spaces[-1]:]
        
        return ans

        
