class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        ans = []
        r1, c1, r2, c2 = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            for j in range(c1, c2 + 1):
                ans.append(matrix[r1][j])
            r1 += 1

            for i in range(r1, r2 + 1):
                ans.append(matrix[i][c2])
            c2 -= 1

            if r1 <= r2:
                for j in range(c2, c1 - 1, -1):
                    ans.append(matrix[r2][j])
                r2 -= 1

            if c1 <= c2:
                for i in range(r2, r1 - 1, -1):
                    ans.append(matrix[i][c1])
                c1 += 1

        return ans
