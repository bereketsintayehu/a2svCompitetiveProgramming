class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        cur = []
        def backtrack(ind):
            if len(cur) == k and sum(cur) == n:
                ans.append(cur.copy())
            
            for i in range(ind, 10):
                if sum(cur) < n:
                    cur.append(i)
                    backtrack(i + 1)
                    cur.pop()
        
        backtrack(1)
        return ans