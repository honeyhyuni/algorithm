# https://www.acmicpc.net/problem/1063
arr = [[0] * 8 for i in range(8)]
a, b, c = map(str, input().split())
x, y = 8-int(a[1]), ord(a[0])-65
x1, y1 = 8-int(b[1]), ord(b[0])-65
arr[x][y] = 2
arr[x1][y1] = 1
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
dic = {"R": 0, "L": 1, "B": 2, "T": 3, "RT": 4, "LT": 5, "RB": 6 , "LB": 7}
for i in range(int(c)):
    k = input()
    d = dic[k]
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < 8 and 0 <= ny < 8):
        continue
    if nx == x1 and ny == y1:
        nx1 = x1 + dx[d]
        ny1 = y1 + dy[d]
        if not (0 <= nx1 < 8 and 0 <= ny1 < 8):
            continue
        x1, y1 = nx1, ny1
    x, y = nx, ny
print(chr(y+65)+str(abs(x-8)))
print(chr(y1+65)+str(abs(x1-8)))
