import math
l=list(map(int,input().strip().split()))
n, m, a = l
print(math.ceil(n/a) + math.ceil(m/a))
