class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        mon = 1

        for i in range(1, n//7 + 1):
            ans += sum(range(i, i+7))
            mon += 1
            
        ans += sum(range(mon, n % 7 + mon))
        return ans
        