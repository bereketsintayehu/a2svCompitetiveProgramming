class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr = [['u'] * n for _ in range(m)]
        
        for i, j in walls:
            arr[i][j] = 'w'
        
        for i, j in guards:
            arr[i][j] = 'g'
            
            for d in [-1, 1]:
                ci = i + d
                while 0 <= ci < m and arr[ci][j] not in ('w', 'gr', 'g'):
                    arr[ci][j] = 'gr'
                    ci += d
                
                cj = j + d
                while 0 <= cj < n and arr[i][cj] not in ('w', 'gc', 'g'):
                    arr[i][cj] = 'gc'
                    cj += d
                
                

        for a in arr:
            print(a)
        
        return sum([1 if arr[i][j] == 'u' else 0 for i in range(m) for j in range(n)])
                    
                
            
            