# https://www.acmicpc.net/problem/1965
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1]
for i in range(1, n):
    dp_arr = []
    for j in range(i):
        if arr[i] > arr[j]:
            dp_arr.append(dp[j]+1)
    if not dp_arr:
        dp.append(1)
    else:
        dp.append(max(dp_arr))
print(max(dp))