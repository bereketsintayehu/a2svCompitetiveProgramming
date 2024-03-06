class Solution:
    def totalNQueens(self, n: int) -> int:
        row = [1] * n
        col = [1] * n
        diag = defaultdict(lambda : 1)
        diag2 = defaultdict(lambda : 1)
        
        ans = 0
        def backtrack(j):
            nonlocal ans
            if j == n:
                ans += 1
            
            for i in range(n):
                if all([row[i], diag[i - j], diag2[i + j]]):
                    row[i] = 0
                    col[j] = 0
                    diag[i - j] = 0
                    diag2[i + j] = 0
                    backtrack(j + 1)
                    row[i] = 1
                    col[j] = 1
                    diag[i - j] = 1
                    diag2[i + j] = 1

        backtrack(0)
        return ans