# https://www.acmicpc.net/problem/1707
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        for _ in arr[x]:
            if visited[_] == 0:
                visited[_] = -visited[x]  # 연결 되어있는 노드 - 로 연결
                q.append(_)
            else:
                if visited[_] == visited[x]:  # 연결되어 있는 노드 +- 값이 같다면 이분 그래프가 아님
                    return False
    return True


K = int(input())
for k in range(K):
    v, e = map(int, input().split())
    arr = [[] for i in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = bfs(i)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")