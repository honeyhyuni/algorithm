# https://www.acmicpc.net/problem/2667
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(arr, a, b):
    n = len(arr)
    q = deque()
    q.append((a, b))
    arr[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()
        for _ in range(4):
            nv = x + dx[_]
            nw = y + dy[_]
            if nv < 0 or nv >= n or nw < 0 or nw >= n:
                continue
            if arr[nv][nw] == 1:
                arr[nv][nw] = 0
                q.append((nv, nw))
                count += 1
    return count


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt.append(bfs(arr, i, j))

cnt.sort()
print(len(cnt))  # 단지 갯수
for i in cnt:
    print(i)    # 단지 크기 오름차순
