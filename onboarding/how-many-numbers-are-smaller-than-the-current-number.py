class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snum = sorted(nums)
        count = {}

        for i, num in enumerate(snum):
            if num not in count:
                count[num] = i
        

        return [count[num] for num in nums]