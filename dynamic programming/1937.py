# https://www.acmicpc.net/problem/1937
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]


def dfs(i, j):
    if dp[i][j] == 0:
        dp[i][j] = 1
        for _ in range(4):
            nx = i + dx[_]
            ny = j + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[i][j]:
                dp[i][j] = max(dp[i][j], dfs(nx, ny))
    return dp[i][j] + 1


for i in range(n):
    for j in range(n):
        dfs(i, j)
print(max(map(max, dp)))