# https://www.acmicpc.net/problem/1005
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    building = [0] + list(map(int, input().split()))
    arr = [[] for i in range(n+1)]
    degree, dp = [0] * (n+1), [0] * (n+1)
    for i in range(m):
        x, y = map(int, input().split())
        arr[x].append(y)
        degree[y] += 1
    goal_building = int(input())
    q = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = building[i]
    while q:
        x = q.popleft()
        for i in arr[x]:
            degree[i] -= 1
            dp[i] = max(dp[x] + building[i], dp[i])
            if degree[i] == 0:
                q.append(i)

    print(dp[goal_building])