class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = [1] * n
        col = [1] * n
        diag = defaultdict(lambda : 1)
        diag2 = defaultdict(lambda : 1)
        
        ans = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(j):
            if j == n:
                ans.append([''.join(b) for b in board])
            
            for i in range(n):
                if all([row[i], diag[i - j], diag2[i + j]]):
                    board[i][j] = 'Q'
                    row[i] = 0
                    col[j] = 0
                    diag[i - j] = 0
                    diag2[i + j] = 0
                    backtrack(j + 1)
                    row[i] = 1
                    col[j] = 1
                    diag[i - j] = 1
                    diag2[i + j] = 1
                    board[i][j] = '.'

        backtrack(0)
        return ans