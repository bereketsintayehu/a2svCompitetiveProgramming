class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0

        while target != 1 and maxDoubles:
            if target % 2:
                ans += 1
                target -= 1
            maxDoubles -= 1
            target //= 2
            ans += 1


        return ans + target - 1