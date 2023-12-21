class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = minimum2 = float('inf')

        for num in nums:
            if num > minimum2:
                return True
            if num <= minimum:
                minimum = num
            else:
                minimum2 = num

        return False