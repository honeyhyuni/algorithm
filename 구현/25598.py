# https://www.acmicpc.net/problem/25598
import sys
input = sys.stdin.readline

dd = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1), "S": (0, 0)}


def move_me(v):
    x, y = me
    dx, dy = dd[v]
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < n and wall[nx][ny] == 0:
        me[0], me[1] = nx, ny


def change_d(x, y, d):
    temp = []
    for i, j in enumerate(["U", "R", "D", "L"]):
        nx, ny = x, y
        dx, dy = dd[j]
        c = 0
        for _ in range(1, n + 1):
            nx += dx
            ny += dy
            if 0 <= nx < n and 0 <= ny < n:
                if wall[nx][ny] == 1:
                    c += 1
            else:
                temp.append((i, c, j))
                break
    temp.sort(key=lambda x: (-x[1], x[0]))
    return temp[0][2]


def move_zombie():
    for i in range(z):
        x, y, v, d, s = zombie[i]
        if v == 0:
            dx, dy = dd[d]
            for _ in range(1, s + 1):
                x += dx
                y += dy
                if not (0 <= x < n and 0 <= y < n and wall[x][y] == 0):
                    x -= dx
                    y -= dy
                    zombie[i][0] = x
                    zombie[i][1] = x
                    if d == "R":
                        zombie[i][3] = "L"
                    elif d == "L":
                        zombie[i][3] = "R"
                    elif d == "U":
                        zombie[i][3] = "D"
                    else:
                        zombie[i][3] = "U"
                    break
            zombie[i][0], zombie[i][1] = x, y
        else:
            dx, dy = dd[d]
            for _ in range(1, s + 1):
                x += dx
                y += dy
                if not(0 <= x < n and 0 <= y < n):
                    x -= dx
                    y -= dy
                    break
                elif wall[x][y] == 1:
                    wall[x][y] = 0
                    x -= dx
                    y -= dy
                    break
            t = change_d(x, y, d)
            zombie[i][0], zombie[i][1], zombie[i][3] = x, y, t


def check():
    x, y = me
    for i in zombie:
        if i[0] == x and i[1] == y:
            return False
    return True


n = int(input())
control = input().rstrip()
me = list(map(int, input().split()))
me[0] -= 1
me[1] -= 1
w = int(input())
wall = [[0] * n for i in range(n)]

for i in range(w):
    a, b = map(int, input().split())
    wall[a - 1][b - 1] = 1
z = int(input())
zombie = []
for i in range(z):
    a, b, c, d, e = map(str, input().split())
    a = int(a)
    b = int(b)
    c = int(c)
    e = int(e)
    zombie.append([a - 1, b - 1, c, d, e])
day = int(input())
for i in range(day):
    move_me(control[i])
    move_zombie()
    if not check():
        print(i + 1)
        print("DEAD...")
        break
else:
    print("ALIVE!")
