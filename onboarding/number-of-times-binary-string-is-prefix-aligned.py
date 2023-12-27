class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        flipCount = 0
        mFlipped = 0

        for flip in flips:
            mFlipped = max(mFlipped, flip)
            flipCount += 1

            if mFlipped == flipCount:
                res += 1
        
        return res