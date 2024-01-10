class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = inf
        map = {}

        for i, card in enumerate(cards):
            if card in map:
                ans = min(ans, i - map[card] + 1)
            map[card] = i

        return ans if ans != inf else -1