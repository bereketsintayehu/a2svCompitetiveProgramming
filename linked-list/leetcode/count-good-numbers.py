class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        if n % 2:
            return pow(20, n // 2, MOD) * 5 % MOD
        else:
            return pow(20, n // 2, MOD) % MOD