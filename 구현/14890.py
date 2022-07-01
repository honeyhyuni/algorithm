# https://www.acmicpc.net/problem/14890
import sys


def load(x):
    visited = [False] * n
    for i in range(n - 1):
        if x[i] == x[i + 1]:
            continue
        elif abs(x[i] - x[i + 1]) > 1:
            return False
        if x[i] > x[i + 1]:
            temp = x[i + 1]
            for _ in range(i + 1, i + 1 + l):
                if 0 <= _ < n and not visited[_]:
                    if x[_] != temp:
                        return False
                    visited[_] = True
                else:
                    return False
        else:
            temp = x[i]
            for _ in range(i, i - l, -1):
                if 0 <= _ < n and not visited[_]:
                    if x[_] != temp:
                        return False
                    visited[_] = True
                else:
                    return False
    return True


input = sys.stdin.readline
n, l = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cnt = 0
for i in arr:
    if load(i):
        cnt += 1
arr = list(zip(*arr))
for i in arr:
    if load(i):
        cnt += 1
print(cnt)
