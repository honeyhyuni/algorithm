# https://www.acmicpc.net/problem/3967
import sys

arr = [list(map(str, input().rstrip())) for i in range(5)]

blank = []
visited = [False] * 12
for i in range(5):
    for j in range(9):
        if arr[i][j] == "x":
            blank.append((i, j))
        elif 65 <= ord(arr[i][j]) <= 77:
            visited[ord(arr[i][j]) - 65] = True


def check():
    o = ord(arr[0][4]) + ord(arr[1][3]) + ord(arr[2][2]) + ord(arr[3][1])
    t = ord(arr[0][4]) + ord(arr[1][5]) + ord(arr[2][6]) + ord(arr[3][7])
    th = ord(arr[1][1]) + ord(arr[1][3]) + ord(arr[1][5]) + ord(arr[1][7])
    fo = ord(arr[3][1]) + ord(arr[3][3]) + ord(arr[3][5]) + ord(arr[3][7])
    fi = ord(arr[4][4]) + ord(arr[3][3]) + ord(arr[2][2]) + ord(arr[1][1])
    si = ord(arr[4][4]) + ord(arr[3][5]) + ord(arr[2][6]) + ord(arr[1][7])
    if o == t == th == fo == fi == si:
        return True
    else:
        return False


def back(cnt):
    if cnt == len(blank):
        if check():
            for i in arr:
                print("".join(i))
            sys.exit()
        return
    x, y = blank[cnt]
    for i in range(12):
        if not visited[i]:
            visited[i] = True
            arr[x][y] = chr(i + 65)
            back(cnt + 1)
            arr[x][y] = "x"
            visited[i] = False


back(0)
