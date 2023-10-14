n = int(input())
arr = list(map(int, input().split()))

even = odd = False

for i in arr:
    if i % 2 == 0:
        even = True
    else:
        odd = True
    if even and odd:
        break
    
if even and odd:
    print(*sorted(arr))
else:
    print(*arr)
