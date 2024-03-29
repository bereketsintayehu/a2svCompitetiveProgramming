class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        i = 0
        ans = 0
        n = len(s)

        while i < n:
            if i != n - 1 and s[i]+s[i+1] in special:
                ans += special[s[i]+s[i+1]]
                i += 2
            else:
                ans += symbol[s[i]]
                i += 1
        
        return ans

