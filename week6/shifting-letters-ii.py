class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * n

        for st, e, di in shifts:
            if di:
                shift[st] += 1
                if e + 1 < n:
                    shift[e + 1] -= 1
            else:
                shift[st] -= 1
                if e + 1 < n:
                    shift[e + 1] += 1
        
        shift = list(accumulate(shift))

        return ''.join([chr(((ord(s[i]) - 97 + shift[i]) % 26) + 97)
for i in range(n)])