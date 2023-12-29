class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -int(''.join(map(str, sorted(map(int, str(num)[1:]), reverse=True))))
        
        num = sorted(map(int, str(num)))
        n, i = len(num), 0

        while i < n - 1 and num[i] == 0:
            i += 1

        return int(''.join(map(str, [num[i]]+[0]*i+num[i+1:])))