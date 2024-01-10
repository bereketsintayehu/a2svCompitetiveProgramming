class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k > n:
            return 0

        curr = ans = sum(cardPoints[:n - k])
        j = 0

        for i in range(n - k, n):
            curr += cardPoints[i] - cardPoints[j]
            j += 1
            ans = min(ans, curr)
        
        return sum(cardPoints) - ans
        