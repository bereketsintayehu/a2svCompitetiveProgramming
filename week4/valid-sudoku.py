class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            s = set()
            for e in row:
                if e in s:
                    return False
                if e != '.':
                    s.add(e)
        
        for col in zip(*board):
            s = set()
            for e in col:
                if e in s:
                    return False
                if e != '.':
                    s.add(e)

        r, c = len(board), len(board[0])
        d = [
            (-1, 0),
            (1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (0, -1),
            (0, 1),
            (0, 0),
            (1, -1)
        ]

        for i in range(1, r - 1, 3):
            for j in range(1, c - 1, 3):
                s = set()
                for dx, dy in d:
                    curr = board[i-dx][j-dy]
                    if curr in s:
                        return False
                    if curr != '.':
                        s.add(curr)

        return True
        


