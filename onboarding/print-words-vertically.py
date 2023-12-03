class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(map(len, words), default=0)
        d = [[] for _ in range(n)]

        for word in words:
            for i, c in enumerate(word):
                d[i].append(c)
            for j in range(i+1, n):
                d[j].append(' ')
        
        return [''.join(d[i]).rstrip() for i in range(n)]

