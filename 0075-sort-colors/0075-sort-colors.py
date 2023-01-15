class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        for i in range(len(nums)):
            if nums[current] == 0:
                nums.pop(current)
                nums.insert(0, 0)
                current += 1
            elif nums[current] == 2:
                nums.pop(current)
                nums.append(2)
            else:
                current += 1