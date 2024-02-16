class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        n = len(points)
        ans = 0
        i = 0

        while i < n:
            x = points[i][1]
            while i < n and points[i][0] <= x <= points[i][1]:
                i += 1
            ans += 1

        return ans