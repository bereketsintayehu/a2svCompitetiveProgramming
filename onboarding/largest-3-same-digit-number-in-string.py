class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        windowStart = 0
        d = defaultdict(int)

        for windowEnd in range(len(num)):
            d[num[windowEnd]] += 1
            
            if windowEnd - windowStart >= 2:
                if len(d) == 1:
                    ans = max(ans, num[windowStart:windowEnd+1])

                d[num[windowStart]] -= 1

                if d[num[windowStart]] == 0:
                    del d[num[windowStart]]
                
                windowStart += 1
        
        return ans
