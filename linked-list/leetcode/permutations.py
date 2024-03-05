class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        s = set()
        bucket = []
        def backtrack(cur):
            if len(s) == len(nums):
                ans.append(bucket.copy())
                return
            
            for num in nums:
                if num not in bucket:
                    s.add(num)
                    bucket.append(num)
                    backtrack(num)
                    s.discard(bucket.pop())
        
        backtrack(-11)
        return ans