class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        
        piles.sort(reverse=True)
        
        for i in range(1, len(piles)-len(piles)//3, 2):
            ans += piles[i]
        
        return ans
