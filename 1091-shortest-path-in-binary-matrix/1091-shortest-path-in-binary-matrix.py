class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        queue = deque([(0, 0, 1)])  
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            row, col, dist = queue.popleft()

            if row == n - 1 and col == n - 1:  
                return dist

            for drow, dcol in directions:
                new_row, new_col = row + drow, col + dcol

                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col, dist + 1))
                    grid[new_row][new_col] = 1  

        return -1  
        