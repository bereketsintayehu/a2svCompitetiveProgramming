class Solution:
    def diagonalSum(self, mat) -> int:
        ans = 0
        n = len(mat)
        
        for i in range(len(mat)):
            ans += mat[i][i]
            if i != n-i-1:
                ans += mat[i][n-i-1]
        
        return ans
