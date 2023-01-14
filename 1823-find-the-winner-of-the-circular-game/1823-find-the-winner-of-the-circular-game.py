class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def findLooser(n, k):
            if (n == 1) :
                return 0
            return ((k + 1) % n + findLooser(n - 1, k)) % n
        return findLooser(n, k - 1) + 1


