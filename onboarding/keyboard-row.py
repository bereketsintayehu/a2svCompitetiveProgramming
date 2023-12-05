class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        rows = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]

        for word in words:
            for row in rows:
                if all(c in row for c in word.lower()):
                    ans.append(word)
                    break

        return ans
        