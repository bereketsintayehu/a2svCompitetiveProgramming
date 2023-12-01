class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienOrder = { ch: i for i, ch in enumerate(order) }
        
        for i in range(len(words)-1):
            if tuple(alienOrder[ch] for ch in words[i]) > tuple(alienOrder[ch] for ch in words[i+1]):
                return False

        return True