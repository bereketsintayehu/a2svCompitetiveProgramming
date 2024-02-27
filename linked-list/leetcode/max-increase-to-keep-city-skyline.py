class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [max(g) for g in grid]
        colMax = [max(g) for g in zip(*grid)]

        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return ans