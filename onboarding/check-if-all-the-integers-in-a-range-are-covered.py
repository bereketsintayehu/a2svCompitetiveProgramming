class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = {i for i in range(left, right+1)}

        for l, r in ranges:
            for i in range(l, r + 1):
                s.discard(i)
        
        return len(s) == 0
