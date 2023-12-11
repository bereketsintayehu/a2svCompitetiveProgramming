class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evenSum = sum([num for num in nums if num % 2 == 0])

        for val, i in queries:
            
            if nums[i] % 2 == 1:
                if val % 2 == 1:
                    evenSum += val + nums[i]
            else:
                if val % 2 == 0:
                    evenSum += val 
                else:
                    evenSum -= nums[i]
            
            nums[i] += val
            ans.append(evenSum)
        
        return ans