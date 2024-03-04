class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        cur = []
        def backtrack(ind, curSum):
            if curSum == target:
                ans.append(cur.copy())
            
            i = ind
            while i < len(candidates):
                if curSum < target:
                    curSum += candidates[i]
                    cur.append(candidates[i])
                    backtrack(i + 1, curSum)
                    curSum -= candidates[i]
                    cur.pop()
                i += 1
                while len(candidates) > i > 0 and candidates[i] == candidates[i - 1]:
                    i += 1

        backtrack(0, 0)
        return ans