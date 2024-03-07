class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(start, i) for i, (start, _) in enumerate(intervals)])
        ans = []
       
        for _, end in intervals:
            indx = bisect_left(starts, (end, 0))
            if indx >= len(intervals):
                ans.append(-1)
            else:
                ans.append(starts[indx][1])

        return ans