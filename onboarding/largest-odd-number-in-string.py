class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        odd = {str(i) for i in range(1, 10, 2)}

        for i, c in enumerate(reversed(num)):
            if c in odd:
                print(i)
                return num[:n - i]
        
        return ''

