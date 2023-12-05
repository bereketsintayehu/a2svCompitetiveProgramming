class Solution:
    def numberOfMatches(self, n: int) -> int:
        plays = 0

        while n != 1:
            plays += n // 2
            n = math.ceil(n/2)
            
        return plays