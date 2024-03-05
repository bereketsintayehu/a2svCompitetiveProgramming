class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        bucket = []
        d = {
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        }
        m, n = len(board), len(board[0])
        def backtrack(r, c, l):
            nonlocal m, n
            if l == len(word):
                print(s)
                return True

            for rd, cd in d:
                i, j = r + rd, c + cd
                if 0 <= i < m and 0 <= j < n:
                    if board[i][j] == word[l] and (i, j) not in s:
                        bucket.append((i, j))
                        s.add((i, j))
                        if backtrack(i, j, l + 1):
                            return True
                        s.discard(bucket.pop())

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    s = set([(i, j)])
                    bucket = [(i, j)]
                    if backtrack(i, j, 1):
                        return True
