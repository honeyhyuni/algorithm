# https://www.acmicpc.net/problem/13265
from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    while q:
        x = q.popleft()
        for _ in arr[x]:
            if not visited[_]:
                visited[_] = visited[x] * -1
                q.append(_)
            else:
                if visited[_] == visited[x]:
                    return False
    return True


T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    visited = [0] * (n + 1)
    # 모든 노드가 연결되어있지 않을수도 있음
    for i in range(1, len(visited)):
        if not visited[i]:
            visited[i] = 1
            q = deque()
            q.append(i)
            if not bfs():
                print("impossible")
                break
    else:
        print("possible")
