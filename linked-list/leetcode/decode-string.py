class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cnt = 0
        cur = []

        for c in s:
            if c.isdigit():
                cnt *= 10 
                cnt += int(c)
            elif c == ']':
                l, n = stack.pop()
                cur = l + cur * n
            elif c == '[':
                stack.append((cur, cnt))
                cur, cnt = [], 0
            else:
                cur.append(c)

        return ''.join(cur)