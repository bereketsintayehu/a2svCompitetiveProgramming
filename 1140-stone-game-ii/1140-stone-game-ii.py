class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            curr_sum = 0
            max_score = float('-inf')

            for x in range(1, 2 * M + 1):
                if i + x <= n:
                    curr_sum += piles[i + x - 1]
                    next_turn_score = dp(i + x, max(M, x))
                    total_score = curr_sum - next_turn_score
                    max_score = max(max_score, total_score)

            memo[(i, M)] = max_score

            return max_score

        return (sum(piles) + dp(0, 1)) // 2


        