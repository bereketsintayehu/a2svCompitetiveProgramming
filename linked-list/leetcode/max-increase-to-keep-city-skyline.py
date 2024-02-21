class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [max(g) for g in grid]
        colMax = [0] * n

        for i in range(n):
            for j in range(n):
                colMax[j] = max(colMax[j], grid[i][j])

        print(colMax)
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return ans