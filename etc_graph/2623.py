# https://www.acmicpc.net/problem/2623
from collections import deque

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    x = list(map(int, input().split()))
    for i in range(x[0]-1):
        arr[x[i+1]].append(x[i+2])
        degree[x[i+2]] += 1
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
            q.append(i)
            result.append(i)

if len(result) == n:
    print("\n".join(map(str, result)))
else:
    print(0)