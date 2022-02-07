# https://www.acmicpc.net/problem/1699
import sys

n = int(input())
dp = [0] * (n+1)
arr = []
for i in range(1, n):
    if i * i > n:
        break
    arr.append(i*i)
dp[1] = 1
for i in range(2, n+1):
    result = sys.maxsize
    for j in arr:
        if j > i:
            break
        result = min(result, dp[i-j])
    dp[i] = result + 1
print(dp[n])