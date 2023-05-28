class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()  
        mergedCuts = [0] + cuts + [n]  
        man = [[0] * len(mergedCuts) for _ in range(len(mergedCuts))]  

        for diagonal in range(2, len(mergedCuts)):
            for i in range(len(mergedCuts) - diagonal):
                j = i + diagonal
                man[i][j] = float('inf')  
                
                for k in range(i+1, j):
                    man[i][j] = min(man[i][j], man[i][k] + man[k][j])

                man[i][j] += mergedCuts[j] - mergedCuts[i]

        return man[0][len(mergedCuts) - 1]  
