class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)

        nums.sort()

        def find_three_sum(i):
            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                two_sum = nums[l] + nums[r]

                if two_sum == target:
                    triplets.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif two_sum > target:
                    r -= 1

                else:
                    l += 1
                

        for i in range(len(nums)):
            if nums[i] > 0:
                break 

            if i > 0 and nums[i-1] == nums[i]:
                continue

            find_three_sum(i)
        
        return triplets

    
        

        