class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wined = set()
        lost = {}

        for winner, losser in matches:
            lost[losser] = lost.get(losser, 0) + 1
            wined.add(winner)
        
        return [[player for player in sorted(wined) if player not in lost], [player for player in sorted(lost.keys()) if lost[player] == 1]]