class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) + 1

        while l + 1 < r:
            mid = (l + r) // 2
            cur = sum([(p + mid - 1) // mid for p in piles])
            
            if cur <= h:
                r = mid
            else:
                l = mid
        
        return r
            