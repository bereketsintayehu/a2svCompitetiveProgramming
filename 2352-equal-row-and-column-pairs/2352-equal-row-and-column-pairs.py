class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = defaultdict(list)
        col = defaultdict(list)
        l = len(grid)
        ans = 0
        
        for i in range(l):
            for j in range(l):
                row[i].append(grid[i][j])
                col[j].append(grid[i][j])
                
        for k in row:
            for c in col:
                if row[k] == col[c]:
                    ans += 1
                    
        return ans