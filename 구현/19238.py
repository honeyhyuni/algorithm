# https://www.acmicpc.net/problem/19238
import sys

input = sys.stdin.readline
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
start_x, start_y = map(int, input().split())
taxi_goal = {}  # 도착지 딕셔너리
for i in range(m):
    x, y, x2, y2 = map(int, input().split())
    arr[x - 1][y - 1] = i + 2
    taxi_goal[i + 2] = [x2 - 1, y2 - 1]

q = deque()
q.append([start_x - 1, start_y - 1])


# 가장 가까운 손님 찾기
def move_taxi():
    global k
    temp = []
    visited = [[0] * n for i in range(n)]
    visited[q[0][0]][q[0][1]] = 1
    if arr[q[0][0]][q[0][1]] != 0:
        temp.append([0, q[0][0], q[0][1], arr[q[0][0]][q[0][1]]])
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if arr[nx][ny] != 0:
                    temp.append([visited[nx][ny] - 1, nx, ny, arr[nx][ny]])
    if not temp:
        return False
    temp.sort(key=lambda x: (x[0], x[1], x[2]))
    v, xx, yy, num = temp[0]
    arr[xx][yy] = 0
    k -= v
    if not go_goal_taxi(xx, yy, num):
        return False
    return True


# 도착지 찾기
def go_goal_taxi(x, y, num):
    global k
    visited = [[0] * n for i in range(n)]
    visited[x][y] = 1
    qq = deque()
    qq.append([x, y])
    while qq:
        x, y = qq.popleft()
        if x == taxi_goal[num][0] and y == taxi_goal[num][1]:
            k -= (visited[x][y] - 1)
            if k < 0:
                return False
            else:
                k += (visited[x][y] - 1) * 2
            q.append([x, y])
            return True
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                qq.append([nx, ny])


while m > 0:
    if not move_taxi():
        print(-1)
        break
    m -= 1
else:
    print(k)
