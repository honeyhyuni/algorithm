# https://www.acmicpc.net/problem/12100
import copy
import sys

input = sys.stdin.readline
from collections import deque

n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

ans = 0


def back(d, cnt, a):
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, a)))
        return
    q = deque()
    if d == 0:
        for i in range(n):
            for j in range(n):
                if a[i][j] != 0:
                    q.append(a[i][j])
            for j in range(n):
                if not q:
                    a[i][j] = 0
                else:
                    if len(q) > 1:
                        if q[0] == q[1]:
                            a[i][j] = q[0] + q[1]
                            q.popleft()
                            q.popleft()
                        else:
                            a[i][j] = q.popleft()
                    else:
                        a[i][j] = q.popleft()
    if d == 1:
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if a[i][j] != 0:
                    q.append(a[i][j])
            for j in range(n - 1, -1, -1):
                if not q:
                    a[i][j] = 0
                else:
                    if len(q) > 1:
                        if q[0] == q[1]:
                            a[i][j] = q[0] + q[1]
                            q.popleft()
                            q.popleft()
                        else:
                            a[i][j] = q.popleft()
                    else:
                        a[i][j] = q.popleft()
    if d == 2:
        for j in range(n):
            for i in range(n):
                if a[i][j] != 0:
                    q.append(a[i][j])
            for i in range(n):
                if not q:
                    a[i][j] = 0
                else:
                    if len(q) > 1:
                        if q[0] == q[1]:
                            a[i][j] = q[0] + q[1]
                            q.popleft()
                            q.popleft()
                        else:
                            a[i][j] = q.popleft()
                    else:
                        a[i][j] = q.popleft()
    if d == 3:
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if a[i][j] != 0:
                    q.append(a[i][j])
            for i in range(n - 1, -1, -1):
                if not q:
                    a[i][j] = 0
                else:
                    if len(q) > 1:
                        if q[0] == q[1]:
                            a[i][j] = q[0] + q[1]
                            q.popleft()
                            q.popleft()
                        else:
                            a[i][j] = q.popleft()
                    else:
                        a[i][j] = q.popleft()

    for i in range(4):
        back(i, cnt + 1, copy.deepcopy(a))


for i in range(4):
    back(i, 0, copy.deepcopy(arr))

print(ans)
