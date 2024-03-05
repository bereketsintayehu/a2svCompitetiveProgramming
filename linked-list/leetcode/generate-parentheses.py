class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        bucket = []
        def backtrack(op, cl):
            if op == cl == n:
                ans.append(''.join(bucket))
                return
            
            if op < n:
                bucket.append('(')
                backtrack(op + 1, cl)
                bucket.pop()

            if op > cl:
                bucket.append(')')
                backtrack(op, cl + 1)
                bucket.pop()


        backtrack(0, 0)
        return ans