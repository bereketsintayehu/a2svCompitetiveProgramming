class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        
        def sortKey(e):
            return e[-1]
        
        words.sort(key=sortKey)
        
        for i in range(0, len(words)):
            words[i] = words[i][:-1]
        
        return ' '.join(words)
        