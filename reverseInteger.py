class Solution:
    def reverse(self, x: int) -> int:
        revx = int(str(abs(x))[::-1]) 
        if x > 0:
            return revx if revx <= 2**31 - 1 else 0
        else:
            return -revx if  -2**31 <= -revx else 0
