# https://www.acmicpc.net/problem/1167
import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [[] for i in range(n + 1)]

for _ in range(n):
    temp = list(map(int, input().split()))
    idx = temp[0]
    for i in range(1, len(temp) - 1, 2):
        arr[idx].append((temp[i], temp[i + 1]))


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    visited[start] = True
    while q:
        node, cnt = q.popleft()
        distance[node] = cnt
        for i, j in arr[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt + j))
    return distance

# 1 에서 bfs 를 한번 돌린뒤 가장 거리가 먼 정점의 인덱스를 구해
# bfs 를 한번 더 돌려준뒤 가장 큰값을 출력한다.
max_v = 0
m = bfs(1)
m2 = m.index(max(m))
print(max(bfs(m2)))