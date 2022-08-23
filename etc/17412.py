# https://www.acmicpc.net/problem/17412
# Network-flow 기본 이론 문제
import sys
from collections import deque


def minus_flow(node):
    if node == 1:
        return
    flow[prev[node]][node] += 1
    flow[node][prev[node]] -= 1
    minus_flow(prev[node])


input = sys.stdin.readline
n, m = map(int, input().split())
capacity = [[0] * (n+1) for i in range(n+1)]
flow = [[0] * (n+1) for i in range(n+1)]
arr = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    capacity[a][b] = 1
    arr[a].append(b)

cnt = 0

while True:
    q = deque()
    q.append(1)
    prev = [-1] * (n + 1)
    while q:
        x = q.popleft()
        if x == 2:
            break
        for n_n in range(1, n + 1):
            if capacity[x][n_n] - flow[x][n_n] > 0 and prev[n_n] == -1:
                prev[n_n] = x
                q.append(n_n)

    if prev[2] == -1:
        break
    cnt += 1
    minus_flow(2)
print(cnt)