class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        bucket = []
        ans = []
        def backtrack(i):
            if i == len(digits) and bucket:
                ans.append(''.join(bucket))
                return 
            
            if i >= len(digits):
                return 

            for c in d[digits[i]]:
                bucket.append(c)
                backtrack(i + 1)
                bucket.pop()
        
        backtrack(0)
        return ans
