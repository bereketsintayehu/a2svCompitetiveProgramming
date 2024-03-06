class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity):
            cur = 0
            cnt = 1
            for weight in weights:
                cur += weight
                if cur > capacity:
                    cnt += 1
                    cur = weight
                if cnt > days:
                    return False

            return cnt <= days
        
        l, h = max(weights) - 1, sum(weights) + 1

        while l + 1 < h:
            mid = (l + h) // 2
            if helper(mid):
                h = mid
            else:
                l = mid
        
        return h
