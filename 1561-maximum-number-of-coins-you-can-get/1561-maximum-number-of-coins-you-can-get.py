import heapq

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        
        nPiles = heapq.nlargest((len(piles) // 3) * 2, piles)
        
        for i in range(1, len(nPiles), 2):
            ans += nPiles[i]
        
        return ans