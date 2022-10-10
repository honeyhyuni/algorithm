# https://www.acmicpc.net/problem/25824
import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(12)]
result = sys.maxsize


def back(v, c, temp):
    global result
    if v >= 10 and c:
        result = min(result, temp)
        return
    if not c:
        if v % 2 == 0:
            back(v + 1, True, temp + arr[v][v + 1])
        else:
            back(v - 1, True, temp + arr[v][v - 1])
    else:
        for _ in [v + 1, v + 2]:
            if v % 2 == 0 and _ + 1 < 12:
                back(_+1, False, temp + arr[v][_+1])
            elif v % 2 == 1 and _ < 12:
                back(_, False, temp + arr[v][_])


back(0, False, 0)
back(1, False, 0)
print(result)