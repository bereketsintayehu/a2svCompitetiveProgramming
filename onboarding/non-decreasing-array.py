class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def isSorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if isSorted(nums[:i-1] + nums[i:]) or isSorted(nums[:i] + nums[i+1:]):
                    return True
                else:
                    return False

        return True