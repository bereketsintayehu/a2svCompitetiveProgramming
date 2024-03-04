class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        cur = []
        def backtrack(ind):
            ans.add(tuple(sorted(cur)))

            for i in range(ind, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1)
                cur.pop()
        
        backtrack(0)
        return ans