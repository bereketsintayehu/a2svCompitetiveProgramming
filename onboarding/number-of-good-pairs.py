class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numCount = defaultdict(int)
        count = 0

        for num in nums:
            count += numCount[num]
            numCount[num] += 1

        return count
        