# https://www.acmicpc.net/problem/4963
dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def bfs(i, j):
    a[i][j] = 0
    q = [[i, j]]
    while q:
        x, y = q[0][0], q[0][1]
        del q[0]
        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == 1:
                a[nx][ny] = 0
                q.append([nx, ny])


while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
