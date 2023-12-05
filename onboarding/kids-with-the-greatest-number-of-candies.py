class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        ans = [True] * len(candies)
        
        for i, c in enumerate(candies):
            if c + extraCandies < ma:
                ans[i] = False
        
        return ans