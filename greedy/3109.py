# https://www.acmicpc.net/problem/3109
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]


def check(x, y):
    arr[x][y] = 'x'
    if y == m - 1:
        return True
    for nx in [x - 1, x, x + 1]:
        if 0 <= nx < n and arr[nx][y + 1] == ".":
            if check(nx, y + 1):
                return True
    return False


result = 0
for i in range(n):
    if check(i, 0):
        result += 1
print(result)