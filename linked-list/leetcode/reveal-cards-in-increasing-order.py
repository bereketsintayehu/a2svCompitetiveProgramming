class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)

        ans = [0] * n
        q = deque([i for i in range(n)])
        
        for d in deck:
            ans[q.popleft()] = d
            if q:
                q.append(q.popleft())
        
        return ans