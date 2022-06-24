# https://www.acmicpc.net/problem/14267
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(v):
    for i in arr[v]:
        dp[i] += dp[v]
        dfs(i)


n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]  # 직속 관계 배열
temp = list(map(int, input().split()))
dp = [0] * (n + 1)  # 칭찬 정도 리스트

for i in range(1, n):
    arr[temp[i]].append(i + 1)

for i in range(m):
    x, y = map(int, input().split())
    dp[x] += y

dfs(1)

print(*dp[1:])
