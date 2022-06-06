# https://www.acmicpc.net/problem/14567
# 위상정렬 기본 이론 문제
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
degree = [0] * (n+1)
arr = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    degree[y] += 1
q = deque()
result = [0] * (n+1)
for i in range(1, n+1):
    if degree[i] == 0:
        q.append((i, 1))
        result[i] = 1
while q:
    x, cnt = q.popleft()
    for i in arr[x]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append((i, cnt+1))
            result[i] = cnt + 1

print(*result[1:])