# https://www.acmicpc.net/problem/14868
import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = [[-1] * n for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()
civiz = deque()
parent = [i for i in range(k)]

for i in range(k):
    x, y = map(int, input().split())
    nx = n - y
    ny = x - 1
    q.append((nx, ny, i))
    civiz.append((nx, ny, i))
    arr[nx][ny] = i


def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union_find(a, b):
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        return True
    return False


def union_civiz():
    global k
    while civiz:
        x, y, v = civiz.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != -1:
                if v != arr[nx][ny]:
                    if union_find(v, arr[nx][ny]):
                        k -= 1
    if k == 1:
        return True
    return False


def bfs():
    for i in range(len(q)):
        x, y, v = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == -1:
                    arr[nx][ny] = v
                    q.append((nx, ny, v))
                    civiz.append((nx, ny, v))
    return union_civiz()


if union_civiz():
    print(0)
else:
    cnt = 0
    while True:
        cnt += 1
        if bfs():
            print(cnt)
            break
