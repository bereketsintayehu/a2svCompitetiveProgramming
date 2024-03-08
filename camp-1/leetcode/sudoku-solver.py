class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[1] * 10 for _ in range(9)]
        col = [[1] * 10 for _ in range(9)]
        box = [[[1] * 10 for _ in range(3)] for __ in range(3)]
        arr = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = int(board[i][j])
                    row[i][cur] = 0
                    col[j][cur] = 0
                    box[i // 3][j // 3][cur] = 0
                else:
                    arr.append((i, j))
        
        def backtrack(r):
            if r == len(arr):
                return True

            i, j = arr[r]
            for c in range(1, 10):
                if row[i][c] and col[j][c] and box[i // 3][j // 3][c]:
                    row[i][c] = 0
                    col[j][c] = 0
                    box[i // 3][j // 3][c] = 0
                    board[i][j] = str(c)

                    if backtrack(r + 1):
                        return True

                    row[i][c] = 1
                    col[j][c] = 1
                    box[i // 3][j // 3][c] = 1

        backtrack(0)