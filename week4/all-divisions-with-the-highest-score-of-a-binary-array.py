class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        rScore = sum(nums)
        lScore = 0

        for i in range(len(nums)):
            d[rScore + lScore].append(i)
            if nums[i]:
                rScore -= 1
            else:
                lScore += 1
                
        d[rScore + lScore].append(len(nums))
        
        return d[max(d)]