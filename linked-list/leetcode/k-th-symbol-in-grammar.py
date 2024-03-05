class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def find(n, k):

            if n == 1:
                return 0
            if k % 2:
                return find(n - 1, (k + 1) // 2) == 1
            else:
                return find(n - 1, k // 2) == 0
            
        return int(find(n , k))

