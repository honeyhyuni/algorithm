# https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
if n == 1: print(arr[0])
elif n == 2: print(sum(arr))
elif n == 3: print(max(arr[0] + arr[2], arr[1] + arr[2]))
else:
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[0] + arr[1], arr[1]))
    dp.append(max(arr[0] + arr[2], arr[1] + arr[2]))
    for i in range(3, n):
        dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
    print(dp[-1])