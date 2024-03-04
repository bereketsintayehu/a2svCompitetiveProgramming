class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        cur = []
        def backtrack(ind, curSum):
            if curSum == target:
                ans.append(cur.copy())

            for i in range(ind, len(candidates)):
                if curSum < target:
                    curSum += candidates[i]
                    cur.append(candidates[i])
                    backtrack(i, curSum)
                    curSum -= candidates[i]
                    cur.pop()
        
        backtrack(0, 0)
        return ans