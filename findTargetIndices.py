class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lCount, tCount = 0, 0

        for num in nums:
            if num < target:
                lCount += 1
            elif num == target:
                tCount += 1

        return [i for i in range(lCount, lCount + tCount)]
