# https://www.acmicpc.net/problem/2252
# 위상정렬 기본 이론문제
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
degree = [0] * (n+1)
arr = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    degree[y] += 1
    arr[x].append(y)

q = deque()
result = []
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)
        result.append(i)
while q:
    x = q.popleft()
    for i in arr[x]:
        degree[i] -= 1
        if degree[i] == 0:
            result.append(i)
            q.append(i)
print(*result)