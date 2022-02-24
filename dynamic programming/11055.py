# https://www.acmicpc.net/problem/11055
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(1, n):
    d = []
    for j in range(i):
        if arr[j] < arr[i]:
            d.append(dp[j] + arr[i])
    if not d:
        dp.append(arr[i])
    else:
        dp.append(max(d))

print(max(dp))