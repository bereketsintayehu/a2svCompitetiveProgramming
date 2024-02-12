from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input()))
    d = defaultdict(int)
    d[0] = 1
    ans = 0
    
    curr = 0
    for i in range(n):
        curr += arr[i]
        ans += d[curr - i - 1]
        d[curr - i - 1] += 1
    
    print(ans)