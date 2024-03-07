class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, cl = len(matrix), len(matrix[0])
        
        l, r = -1, rl * cl
        while l + 1 < r:
            mid = (l + r) // 2
            i, j = mid // cl, mid % cl
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                l = mid
            else:
                r = mid

        return False