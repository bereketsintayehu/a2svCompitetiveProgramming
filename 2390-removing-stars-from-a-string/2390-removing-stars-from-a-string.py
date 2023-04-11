class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for st in s:
            if st == "*":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(st)
        
        return ''.join(stack)
        