class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def compare(num1, num2):
            return int(num1 + num2) - int(num2 + num1)

        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if compare(nums[j], nums[j + 1]) < 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)        