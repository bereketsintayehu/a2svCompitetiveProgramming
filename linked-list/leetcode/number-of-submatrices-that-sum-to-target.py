class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        psum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                psum[i + 1][j + 1] += matrix[i][j] + psum[i+1][j] + psum[i][j + 1] - psum[i][j]
        
        ans = 0

        for r1 in range(n):
            for r2 in range(r1, n):
                count = defaultdict(int)
                count[0] = 1
                for c in range(m):
                    cur = psum[r2 + 1][c + 1] - psum[r1][c + 1]
                    ans += count[cur - target]
                    count[cur] += 1
        
        return ans 