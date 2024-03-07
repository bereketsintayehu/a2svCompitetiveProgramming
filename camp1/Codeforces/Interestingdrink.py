from bisect import bisect_right


n = int(input())
x = sorted(map(int, input().split()))

for _ in range(int(input())):
    m = int(input())
    print(bisect_right(x, m))