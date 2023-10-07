n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = -1
if k == 0:
    ans = nums[0] - 1
elif k == n or nums[k-1] != nums[k]:
    ans = nums[k-1]

if ans >= 1:
    print(ans)
else:
    print(-1)
