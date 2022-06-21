# https://www.acmicpc.net/problem/14002
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1]

for i in range(1, n):
    d = []
    for j in range(i):
        if arr[j] < arr[i]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
idx = dp.index(max(dp))
max_v = dp[idx]

result = [arr[idx]]
for i in range(idx-1, -1, -1):
    if max_v == dp[i] + 1:
        max_v = dp[i]
        result.append(arr[i])
result.sort()

print(max(dp))
print(" ".join(map(str, result)))