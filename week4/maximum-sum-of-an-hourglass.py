class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                curr = sum(grid[row - 1][col - 1:col + 2]) + sum(grid[row + 1][col - 1:col + 2]) + grid[row][col]
                ans = max(ans, curr)

        return ans