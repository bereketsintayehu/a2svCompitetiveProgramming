class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])

        ans = []

        for i in d:
            if i % 2:
                ans.extend(d[i])
            else:
                ans.extend(d[i][::-1])
        
        return ans