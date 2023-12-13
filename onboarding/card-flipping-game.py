class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.discard(fronts[i])

        return min(s) if s else 0