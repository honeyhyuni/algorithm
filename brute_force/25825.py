# https://www.acmicpc.net/problem/25825
import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(12)]
result = sys.maxsize


def back(v, temp, cnt):
    global result
    if cnt == 13:
        result = min(result, temp)
        return
    if cnt % 2 == 0:
        if v % 2 == 0:
            visited[v + 1] = True
            back(v + 1, temp + arr[v][v + 1], cnt+1)
            visited[v + 1] = False
        else:
            visited[v-1] = True
            back(v - 1, temp + arr[v][v - 1], cnt+1)
            visited[v-1] = False
    else:
        for _ in range(12):
            if v % 2 == 0 and _ + 1 < 12 and not visited[_+1]:
                visited[_+1] = True
                back(_ + 1, temp + arr[v][_ + 1], cnt+1)
                visited[_+1] = False
            elif v % 2 == 1 and _ < 12 and not visited[_]:
                visited[_] = True
                back(_, temp + arr[v][_], cnt+1)
                visited[_] = False


visited = [False] * 12
for i in range(12):
    visited[i] = True
    back(i, 0, 1)
    visited[i] = False
print(result)