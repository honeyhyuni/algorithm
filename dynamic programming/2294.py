# https://www.acmicpc.net/problem/2294
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = sorted(list(set(int(input()) for i in range(n))))
dp = [sys.maxsize] * (k+1)

for i in arr:
    for j in range(i, k+1):
        if j % i == 0:
            dp[j] = j // i
        else:
            dp[j] = min(dp[j], dp[j-i] + 1)
print(dp[-1] if dp[-1] != sys.maxsize else -1)