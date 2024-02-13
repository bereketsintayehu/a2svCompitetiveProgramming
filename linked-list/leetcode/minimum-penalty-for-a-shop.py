class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans = n - 1
        m = n

        pre = list(accumulate(map(lambda x: int(x == 'N'), customers), initial=0))
        suff = list(accumulate(map(lambda x: int(x == 'Y'), customers[::-1]), initial=0))[::-1]
        
        for i in range(n + 1):
            if pre[i] + suff[i] < m:
                m = pre[i] + suff[i]
                ans = i
        
        return ans