class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')' : '(', '}': '{', ']': '['}

        for b in s:
            if b in pair:
                if not stack or stack.pop() != pair[b]:
                    return 0
            else:
                stack.append(b)

        return not stack    