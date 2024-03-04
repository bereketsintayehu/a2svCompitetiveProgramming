class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        cur = []
        def backtrack(ind):
            ans.append(cur.copy())

            for i in range(ind, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1)
                cur.pop()
        
        backtrack(0)
        return ans